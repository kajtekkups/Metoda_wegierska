#Algorytm wegierski

import numpy as np


class AlgorytmWegierski:
    def __init__(self, macierz):
        self.macierz = macierz

        self.listaKolumnZerNiezaleznych = []
        self.listaWierszyZerNiezaleznych = []
        self.listaKolumnZeZaleznych = []
        self.listaZerNiezaleznych = {} # lista przechowuje zera niezalezne w formacie listaZerNiezaleznych[kolumna] = wiersz


        self.suma_redukcji_phi = 0
        self.listaWykreslen = [[],  #pierwszy element jest listą rzedow z zerami niezaleznymi
                               []]  #drugi lista kolumn z zerami niezaleznymi

        self.wykresloneWiersze =[]
        self.wykresloneKolumny = []


    def wykreslLinie(self):
        listaNieOznakowanychWierszy = []
        listaOznakowanychKolumn = []
        for index, row in enumerate(self.macierz):

            # nie oznaczac wierszy posiadajacych niezalezne 0
            if index in self.listaWierszyZerNiezaleznych:
               listaNieOznakowanychWierszy.append(index)

            else:
                #oznaczyc kazda kolumne majaca zero zalezne w wierszu oznaczonym
                for col_index, element in enumerate(row):
                    if element == 0:
                        if col_index in self.listaKolumnZeZaleznych:
                            listaOznakowanychKolumn.append(col_index)

                            # oznacz kazdy wiersz majacy w oznakowanej kolumnie niezalezne zero
                            if self.listaZerNiezaleznych[col_index]:
                                try:
                                    listaNieOznakowanychWierszy.remove(self.listaZerNiezaleznych[col_index])
                                except ValueError:
                                    print(f"Element nie istnieje w liście.")

        self.wykresloneWiersze = listaNieOznakowanychWierszy
        self.wykresloneKolumny = listaOznakowanychKolumn


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


    def sprawdzCzyNiezalezne(self, elementRow, elementCol):
        #sprawdz czy w wierszu jest juz zero
        if elementRow in self.listaWierszyZerNiezaleznych:
            return False

        #sprawdz czy w kolumnie jest juz zero
        if elementCol in self.listaKolumnZerNiezaleznych:
            return False

        return True


    def znajdzZeraNiezalezne(self):
        #zanjdz zera w tablicy
        for zeroRowIndex, matrixRow in enumerate(self.macierz):
            for zeroColIndex, matrixElement in enumerate(matrixRow):
                if matrixElement == 0:
                    # ozanacz jako zalezne albo niezalezne
                    if self.sprawdzCzyNiezalezne(zeroRowIndex, zeroColIndex):
                        self.listaKolumnZerNiezaleznych.append(zeroColIndex)
                        self.listaWierszyZerNiezaleznych.append(zeroRowIndex)
                        self.listaZerNiezaleznych[zeroColIndex] = zeroRowIndex
                    else:
                        self.listaKolumnZeZaleznych.append(zeroColIndex)



def main():
    A = np.array([[5, 2, 3, 2, 7],
                  [6, 8, 4, 2, 5],
                  [6, 4, 3, 7, 2],
                  [6, 9, 0, 4, 0],
                  [4, 1, 2, 4, 0]])


    Test = AlgorytmWegierski(A)
    Test.matrix_redux()
    Test.znajdzZeraNiezalezne()
    Test.wykreslLinie()


    print(Test.wykresloneWiersze)
    print(Test.wykresloneKolumny)

    # print(Test.listaKolumnZerNiezaleznych)
    # print(Test.listaWierszyZerNiezaleznych)
    # print(Test.listaZerNiezaleznych)
    # print(Test.macierz)


if __name__ == '__main__':
    main()







