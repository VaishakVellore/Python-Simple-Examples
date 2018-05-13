from numpy import asarray


def square_matrix_multiply(a, b):
    n = len(a)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            result[i][j] = 0
            for k in range(0, n, 1):
                result[i][j] = result[i][j] + a[i][k]*b[k][j]

    return result


def test():
    A = asarray([[0, 0], [0, 0]])
    B = asarray([[0, 0], [0, 0]])
    A = asarray(A)
    B = asarray(B)

    assert A.shape == B.shape
    assert A.shape == A.T.shape

    print(square_matrix_multiply(A, B))
    pass


if __name__ == '__main__':

    test()

