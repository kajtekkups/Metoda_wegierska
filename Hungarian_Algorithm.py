#Algorytm wegierski

import numpy as np


class AlgorytmWegierski:
    def __init__(self, macierz):
        self.macierz = macierz

        # lista przechowuje zera niezalezne w formacie lista[wiersz] = numer kolumny
        self.listaZerNiezaleznych = [None for i in range(len(self.macierz))]
        self.suma_redukcji_phi = 0

        self.zeroZalezne = 9999

    def sprawdzCzyNiezalezne(self, elementRow, elementCol):
        #sprawdz czy w wierszu jest juz zero
        if self.listaZerNiezaleznych[elementRow] is not None:
            return False

        #sprawdz czy w kolumnie jest juz zero
        for zeroListElement in self.listaZerNiezaleznych:
            if zeroListElement == elementCol:
                return False

        return True


    def znajdzZeraNiezalezne(self):
        #zanjdz zera w tablicy
        for zeroRowIndex, matrixRow in enumerate(self.macierz):
            for zeroColIndex, matrixElement in enumerate(matrixRow):
                if matrixElement == 0:
                    # ozanacz jako zalezne albo niezalezne
                    if self.sprawdzCzyNiezalezne(zeroRowIndex, zeroColIndex):
                        self.listaZerNiezaleznych[zeroRowIndex] = zeroColIndex
                    else:
                        self.macierz[zeroRowIndex][zeroColIndex] = self.zeroZalezne


    def matrix_redux(self):

        for row in range(len(self.macierz)):
            #zredukuj wiersze
            min_element_row = min(self.macierz[row])
            self.macierz[row] = self.macierz[row] - min_element_row
            self.suma_redukcji_phi += min_element_row

        #zredukuj kolumny
        for col in range(len(self.macierz)):
            min_element_col = min(self.macierz[:, col])
            self.macierz[:, col] = self.macierz[:, col] - min_element_col
            self.suma_redukcji_phi += min_element_col


def main():
    A = np.array([[5, 2, 3, 2, 7],
                  [6, 8, 4, 2, 5],
                  [6, 4, 3, 7, 2],
                  [6, 9, 0, 4, 0],
                  [4, 1, 2, 4, 0]])


    Test = AlgorytmWegierski(A)
    Test.matrix_redux()
    Test.znajdzZeraNiezalezne()
    # print(Test.listaZerNiezaleznych)
    print(Test.macierz)


if __name__ == '__main__':
    main()







