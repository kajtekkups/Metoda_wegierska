import numpy as np

def matrix_redux(A):
    shape_A = A.shape
    A_1 = np.zeros(shape = shape_A, dtype = int)
    A_2 = np.zeros(shape = shape_A, dtype = int)
    phi = 0
    for x in range(0, shape_A[0]):
        y = min(A[x,:])
        A_1[x,:] = A[x,:] - y
        phi += y

    for x in range(0, shape_A[0]):
        z = min(A_1[:,x])
        A_2[:,x] = A_1[:,x] - z
        phi += z

    return A_1, A_2, phi

def matrix_redux_back(A):
    shape_A = A.shape
    A_1 = np.zeros(shape = shape_A, dtype = int)
    A_2 = np.zeros(shape = shape_A, dtype = int)
    phi = 0
    for x in range(0, shape_A[0]):
        y = min(A[:,x])
        A_2[:,x] = A[:,x] - y
        phi += y

    for x in range(0, shape_A[0]):
        z = min(A_2[x,:])
        A_1[x,:] = A_2[x,:] - z
        phi += z
    
    return A_2, A_1, phi


def main():
    A = np.array([[5,2,3,2,7],[6,8,4,2,5],[6,4,3,7,2],[6,9,0,4,0],[4,1,2,4,0]])
    
    A1, phi = matrix_redux(A)
    A2, phi1 = matrix_redux_back(A)
    print(A1)
    print(phi)
    print()
    print(A2)
    print(phi1)
    

if __name__ == '__main__':
    main()

