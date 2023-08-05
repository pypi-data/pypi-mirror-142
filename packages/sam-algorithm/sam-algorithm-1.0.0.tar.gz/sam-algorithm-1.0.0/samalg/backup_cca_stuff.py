def CCA(X, Y):
    X = StandardScaler().fit_transform(X)
    Y = StandardScaler().fit_transform(Y)
    
    u, w, v = np.linalg.svd(X.T.dot(Y) / (X.shape[0]))
    u, v = svd_flip(u,v)

    wix = np.argsort(-w)
    u = u[:,wix]
    w = w[wix]
    v = v[wix]
    
    return X.dot(u),Y.dot(v.T),w

def batch_kpca(pcas, comps, datas, means, gkeeps, alpha=0.5, n_components=150, seed=0, solver='arpack'):
    
    eta = (1-alpha) - np.zeros((len(pcas),len(pcas)))
    eta[np.arange(eta.shape[0]),np.arange(eta.shape[0])] = alpha
    
    Ks = [[None]*len(pcas) for i in range(len(pcas))]    
    for i in range(len(pcas)):
        for j in range(i,len(pcas)):
            if i==j:
                Ks[i][i] = block_diag(*[Normalizer().fit_transform(p) for p in pcas])
            else:
                Xx = pcas[i]
                Xy = datas[i].dot(comps[j][gkeeps[i]]) - means[i][gkeeps[i]].dot(comps[j][gkeeps[i]])

                Yy = pcas[j]
                Yx = datas[j].dot(comps[i][gkeeps[j]]) - means[j][gkeeps[j]].dot(comps[i][gkeeps[j]])
                X,Y = np.vstack((Xx,Yx)),np.vstack((Xy,Yy))

                u,v,w = CCA(X,Y)
                
                Ks[i][j] = np.hstack((Normalizer().fit_transform(u),Normalizer().fit_transform(v)))/2
                Ks[j][i] = np.hstack((Normalizer().fit_transform(u),Normalizer().fit_transform(v)))/2

            Ks[i][j] *= eta[i,j]**0.5
            Ks[j][i] *= eta[j,i]**0.5
    
    ZEROS = np.zeros((Ks[0][1].shape))
    
    YS1 = []
    YS2 = []
            
    for I in range(len(Ks)):
        rows = []
        for i in range(len(Ks)):
            row = []
            for j in range(len(Ks)):
                if i == I and j != I:
                    row.append(Ks[I][j])
                else:
                    row.append(ZEROS)
            rows.append(np.hstack(row))
        YS1.append(np.vstack(rows))
        
        rows = []
        for i in range(len(Ks)):
            row = []
            for j in range(len(Ks)):
                if i == j and i != I:
                    row.append(Ks[I][j].T)
                else:
                    row.append(ZEROS.T)
            rows.append(np.hstack(row))
        YS2.append(np.vstack(rows))            
    
    rows = []
    for i in range(len(Ks)):
        row = []
        for j in range(len(Ks)):
            if i == j:
                row.append(Ks[i][i])
            else:
                row.append(ZEROS)
        rows.append(np.hstack(row))
    Y = np.vstack(rows)
    
    
    #"""
    def h(x):
        y = np.zeros_like(x)
        y+=Y.dot(Y.T.dot(x))
        for i in range(len(YS1)):
            y+=YS1[i].dot(YS2[i].dot(x))
        return y

    C = sp.linalg.LinearOperator(
        matvec=h,
        dtype=YS1[0].dtype,
        matmat=h,
        shape=(YS1[0].shape[0],YS1[0].shape[0]),
        rmatvec=h,
        rmatmat=h,
    )        

    ones = np.ones(C.shape[0])[None, :].dot
    onesT = np.ones(C.shape[0])[:, None].dot    
    O = sp.diags(np.ones(C.shape[0])).tocsr()

    def p(x):
        return O.dot(x) - onesT(ones(x))/C.shape[0]

    H = sp.linalg.LinearOperator(
        matvec=p,
        dtype=C.dtype,
        matmat=p,
        shape=C.shape,
        rmatvec=p,
        rmatmat=p,
    )

    def M(x):
        return H.dot(C.dot(H.dot(x)))

    XL = sp.linalg.LinearOperator(
        matvec=M,
        dtype=C.dtype,
        matmat=M,
        shape=C.shape,
        rmatvec=M,
        rmatmat=M,
    )
    
    if solver == 'arpack':
        random_init = _init_arpack_v0(C.shape[0],seed)    
        u, w, v = sp.linalg.svds(XL, which="LM", k=n_components, v0=random_init)
        u, v = svd_flip(u,v)
    elif solver == 'randomized':
        u,w,v = randomized_svd(XL,n_components=n_components,n_iter='auto',flip_sign=True,random_state=seed)    

    wix = np.argsort(-w)
    u = u[:,wix]
    w = w[wix]    
    Z = u*w**0.5
    Zs = []
    for i in range(len(Ks)):
        Zs.append(Z[i*Ks[0][0].shape[0] : (i+1)*Ks[0][0].shape[0]])
    Zs = np.hstack(Zs)
    return Zs  
    
def _init_arpack_v0(size, random_state):
    from sklearn.utils import check_random_state
    random_state = check_random_state(random_state)
    v0 = random_state.uniform(-1, 1, size)
    return v0

def randomized_range_finder(A, *, size, n_iter,
                            power_iteration_normalizer='auto',
                            random_state=None):
    import numpy as np
    from scipy import linalg, sparse
    from sklearn.utils import check_random_state
    from sklearn.utils.extmath import svd_flip
    
    random_state = check_random_state(random_state)

    # Generating normal random vectors with shape: (A.shape[1], size)
    Q = random_state.normal(size=(A.shape[1], size))
    if A.dtype.kind == 'f':
        # Ensure f32 is preserved as f32
        Q = Q.astype(A.dtype, copy=False)

    # Deal with "auto" mode
    if power_iteration_normalizer == 'auto':
        if n_iter <= 2:
            power_iteration_normalizer = 'none'
        else:
            power_iteration_normalizer = 'LU'

    # Perform power iterations with Q to further 'imprint' the top
    # singular vectors of A in Q
    for i in range(n_iter):
        if power_iteration_normalizer == 'none':
            Q = A.dot(Q)
            Q = A.T.dot(Q)
        elif power_iteration_normalizer == 'LU':
            Q, _ = linalg.lu(A.dot(Q), permute_l=True)
            Q, _ = linalg.lu(A.T.dot(Q), permute_l=True)
        elif power_iteration_normalizer == 'QR':
            Q, _ = linalg.qr(A.dot(Q), mode='economic')
            Q, _ = linalg.qr(A.T.dot(Q), mode='economic')

    # Sample the range of A using by linear projection of Q
    # Extract an orthonormal basis
    Q, _ = linalg.qr(A.dot(Q), mode='economic')
    return Q

def randomized_svd(M, n_components, *, n_oversamples=10, n_iter='auto',
                   power_iteration_normalizer='auto', transpose='auto',
                   flip_sign=True, random_state=0):
    import numpy as np
    from scipy import linalg, sparse
    from sklearn.utils import check_random_state
    from sklearn.utils.extmath import svd_flip
    
    
    if isinstance(M, (sparse.lil_matrix, sparse.dok_matrix)):
        warnings.warn("Calculating SVD of a {} is expensive. "
                      "csr_matrix is more efficient.".format(
                          type(M).__name__),
                      sparse.SparseEfficiencyWarning)

    random_state = check_random_state(random_state)
    n_random = n_components + n_oversamples
    n_samples, n_features = M.shape

    if n_iter == 'auto':
        # Checks if the number of iterations is explicitly specified
        # Adjust n_iter. 7 was found a good compromise for PCA. See #5299
        n_iter = 7 if n_components < .1 * min(M.shape) else 4

    if transpose == 'auto':
        transpose = n_samples < n_features
    if transpose:
        # this implementation is a bit faster with smaller shape[1]
        M = M.T
    

    Q = randomized_range_finder(
        M, size=n_random, n_iter=n_iter,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state)
    # project M to the (k + p) dimensional space using the basis vectors
    B = M.T.dot(Q).T

    # compute the SVD on the thin matrix: (k + p) wide
    Uhat, s, Vt = linalg.svd(B, full_matrices=False)

    del B
    U = np.dot(Q, Uhat)

    if flip_sign:
        if not transpose:
            U, Vt = svd_flip(U, Vt)
        else:
            # In case of transpose u_based_decision=false
            # to actually flip based on u and not v.
            U, Vt = svd_flip(U, Vt, u_based_decision=False)

    if transpose:
        # transpose back the results according to the input convention
        return Vt[:n_components, :].T, s[:n_components], U[:, :n_components].T
    else:
        return U[:, :n_components], s[:n_components], Vt[:n_components, :]
  
