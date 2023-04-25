#Algorytm wegierski

import numpy as np

matrixExample = [[0, 0, 1, 0, 5],
                 [1, 6, 2, 0, 3],
                 [1, 2, 1, 5, 0],
                 [3, 9, 0, 4, 0],
                 [1, 1, 2, 4, 0]]

def SprawdzCzyNiezalezne(elementRow, elementCol, listaZerNiezaleznych):
    #sprawdz czy w wierszu jest juz zero
    if listaZerNiezaleznych[elementRow] is not None:
        return False

    #sprawdz czy w kolumnie jest juz zero
    for zeroListElement in listaZerNiezaleznych:
        if zeroListElement == elementCol:
            return False

    return True

def ZeraNiezalezne(matrix):

    # lista przechowuje zera niezalezne w formacie lista[wiersz] = numer kolumny
    listaZerNiezaleznych = [None for i in range(len(matrix))]

    for zeroRowIndex, matrixRow in enumerate(matrix):
        for zeroColIndex, matrixElement in enumerate(matrixRow):
            if matrixElement == 0:
                if SprawdzCzyNiezalezne(zeroRowIndex, zeroColIndex, listaZerNiezaleznych):
                    listaZerNiezaleznych[zeroRowIndex] = zeroColIndex

    return listaZerNiezaleznych

print(ZeraNiezalezne(matrixExample))

