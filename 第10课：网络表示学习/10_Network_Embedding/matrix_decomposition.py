import numpy as np

def get_cost(X, U, V, lamb):
    ''' J = |X-UV|_22 + lamb*(|U|_22+|V|_22)
        Input: X [n, d], U [n, m], V [m, d] 
    '''
    UV = np.dot(U, V) 
    cost1 = np.sum((X - UV)**2)

    cost2 = np.sum(U**2) + np.sum(V**2)

    #print('cost1 is %f, cost2 is %f' % (cost1, cost2) )
    res = cost1 + lamb*cost2
    #print('Total cost is %f' % res)
    return res

def mf(X, m, lamb=0.1, learnRate=0.01):
    ''' J = |X-UV|_22 + lamb*(|U|_22+|V|_22)
        Input: G [n, d] 
        Return: U [n, m], V [m, n]
    '''
    maxIter = 50
    n, d = X.shape
    
    #Random initialization:
    U = np.random.random([n, m])/n
    V = np.random.random([m, d])/m

    # Gradient Descent:
    trainRMSE_old = get_cost(X, U, V, lamb) 
    print('cost at iteration start : %f' % trainRMSE_old)
    iter_num = 1 
    while iter_num < maxIter:
        dU = 2*( -np.dot(X, V.T) + np.linalg.multi_dot([U, V, V.T])  + lamb*U ) 
        U = U - learnRate * dU
        trainRMSE_new = get_cost(X, U, V, lamb)
        #print('after update U : %f' % trainRMSE_new)
        
        dV = 2*( -np.dot(U.T, X) + np.linalg.multi_dot([U.T, U, V]) + lamb*V  )
        V = V - learnRate * dV
        trainRMSE_new = get_cost(X, U, V, lamb)
        #print('after update V : %f' % trainRMSE_new)

        if(iter_num%20 == 0): 
            print('cost at iteration %d : %f' % (iter_num, trainRMSE_new))

        iter_num += 1
    return U, V

