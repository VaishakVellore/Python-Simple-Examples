from numpy import asarray


def add(A, B):
    n = len(A)
    result = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            result[i][j] = A[i][j] + B[i][j]
    return result


def subtract(A, B):
    n = len(A)
    result = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            result[i][j] = A[i][j] - B[i][j]
    return result


def square_matrix_multiply_strassens(A, B):
    n = len(A)

    if n == 1:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, n):
            for j in range(0, n):
                C[i][j] = A[i][j] * B[i][j]
        return C
    else:  # dividing the input matrices A and B
        new_length = int(n / 2)

    a11 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    a12 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    a21 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    a22 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]

    b11 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    b12 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    b21 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    b22 = [[0 for i in range(0, new_length)] for j in range(0, new_length)]

    aTemp = [[0 for i in range(0, new_length)] for j in range(0, new_length)]
    bTemp = [[0 for i in range(0, new_length)] for j in range(0, new_length)]

    for i in range(0, new_length):
        for j in range(0, new_length):
            a11[i][j] = A[i][j]
            a12[i][j] = A[i][j + new_length]
            a21[i][j] = A[i + new_length][j]
            a22[i][j] = A[i + new_length][j + new_length]

            b11[i][j] = B[i][j]
            b12[i][j] = B[i][j + new_length]
            b21[i][j] = B[i + new_length][j]
            b22[i][j] = B[i + new_length][j + new_length]

    aTemp = add(a11, a22)
    bTemp = add(b11, b22)
    p1 = square_matrix_multiply_strassens(aTemp, bTemp)

    aTemp = add(a21, a22)
    p2 = square_matrix_multiply_strassens(aTemp, b11)

    bTemp = subtract(b12, b22)
    p3 = square_matrix_multiply_strassens(a11, bTemp)

    bTemp = subtract(b21, b11)
    p4 = square_matrix_multiply_strassens(a22, bTemp)

    aTemp = add(a11, a12)
    p5 = square_matrix_multiply_strassens(aTemp, b22)

    aTemp = subtract(a21, a11)
    bTemp = add(b11, b12)
    p6 = square_matrix_multiply_strassens(aTemp, bTemp)

    aTemp = subtract(a12, a22)
    bTemp = add(b21, b22)
    p7 = square_matrix_multiply_strassens(aTemp, bTemp)

    aTemp = add(p1, p4)
    bTemp = add(aTemp, p7)
    c11 = subtract(bTemp, p5)
    c12 = add(p3, p5)
    c21 = add(p2, p4)

    aTemp = add(p1, p3)
    bTemp = add(aTemp, p6)
    c22 = subtract(bTemp, p2)

    C = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, new_length):
        for j in range(0, new_length):
            C[i][j] = c11[i][j]
            C[i][j + new_length] = c12[i][j]
            C[i + new_length][j] = c21[i][j]
            C[i + new_length][j + new_length] = c22[i][j]
    return C


def test():
    A = asarray([[0, 0], [0, 0]])
    B = asarray([[0, 0], [0, 0]])
    A = asarray(A)
    B = asarray(B)

    assert A.shape == B.shape
    assert A.shape == A.T.shape

    assert (len(A) & (len(A) - 1)) == 0, "A is not a power of 2"

    print(square_matrix_multiply_strassens(A, B))
    pass


if __name__ == '__main__':

    test()

