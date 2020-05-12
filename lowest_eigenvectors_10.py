def square_matrix():
    from numpy import zeros, linalg, linspace, sqrt, sin, pi, sum, sort
    A = zeros([5, 5])

    n = 0
    while n <= 4:
        A[n, n] = 2
        n = n + 1

    n = 0
    while n <= 3:
        A[n, n + 1] = 1
        A[n + 1, n] = 1
        n = n + 1

    H = (1/ (1/4)) * A
    return H


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    from numpy import linalg, linspace, sqrt, sin, pi, sum, sort, argsort

    M_rows = len(square_matrix)
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("Square matrix must have M rows and M columns, M >= 1.")

    (V, D) = linalg.eig(square_matrix)
    ordered_indices = argsort(V)
    eigenvalues = (V[ordered_indices[0:number_of_eigenvectors]])
    eigenvectors = (D[ordered_indices[0:number_of_eigenvectors]])
    return eigenvalues, eigenvectors
