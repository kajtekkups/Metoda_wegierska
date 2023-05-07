#Algorytm wegierski

import numpy as np


class AlgorytmWegierski:
    def __init__(self, macierz):
        self.macierz = macierz

        self.listaZeZaleznych = [[] for i in range(len(self.macierz))] # lista przechowuje zera zalezne w formacie listaZerZaleznych[kolumna] = [wiersze]
        self.listaZerNiezaleznych = {} # lista przechowuje zera niezalezne w formacie listaZerNiezaleznych[kolumna] = wiersz

        self.suma_redukcji_phi = 0

        self.wykresloneWiersze =[]
        self.wykresloneKolumny = []


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


    def znajdzZeraNiezalezne(self):
        #zanjdz zera w tablicy
        for zeroRowIndex, matrixRow in enumerate(self.macierz):
            for zeroColIndex, matrixElement in enumerate(matrixRow):
                if matrixElement == 0:
                    # ozanacz jako zalezne albo niezalezne
                    if self.sprawdzCzyNiezalezne(zeroRowIndex, zeroColIndex):
                        self.listaZerNiezaleznych[zeroColIndex] = zeroRowIndex
                    else:
                        if zeroRowIndex not in self.listaZeZaleznych[zeroColIndex]:
                            self.listaZeZaleznych[zeroColIndex].append(zeroRowIndex)


    def sprawdzCzyNiezalezne(self, elementRow, elementCol):
        #sprawdz czy w wierszu jest juz zero
        if elementRow in self.listaZerNiezaleznych.values():
            return False

        #sprawdz czy w kolumnie jest juz zero
        if elementCol in self.listaZerNiezaleznych.keys():
            return False

        return True


    def wykreslKolumny(self, listaOznakowanychWierszy, lista_sprawdzajaca):
        listaOznakowanychKolumn = []

        # oznaczyc kazda kolumne majaca zero zalezne w wierszach
        for wiersz in listaOznakowanychWierszy:
            for col_index, col_element in enumerate(self.macierz[wiersz]):
                if col_element == 0:
                    # jezeli zero w kolumnie jest zalezne
                    if self.listaZeZaleznych[col_index]:
                        if col_index not in lista_sprawdzajaca:
                            listaOznakowanychKolumn.append(col_index)
        return listaOznakowanychKolumn

    def wykreslLinie(self):
        listaOznakowanychWierszy = []
        listaOznakowanychKolumn = []
        for row_index, row in enumerate(self.macierz):
            #oznaczyc wiersz nie posiadajacy niezaleznego 0
            if row_index not in self.listaZerNiezaleznych.values():
                listaOznakowanychWierszy.append(row_index)

        # oznaczyc kazda kolumne majaca zero zalezne w wierszach

        kolumny_do_wykreslenia = self.wykreslKolumny(listaOznakowanychWierszy, listaOznakowanychKolumn)
        listaOznakowanychKolumn.extend(kolumny_do_wykreslenia)
        while True:
            tymczasowe_wiersze = []

            # oznacz kazdy wiersz majacy w oznakowanej kolumnie niezalezne zero
            for col in kolumny_do_wykreslenia:
                if col in self.listaZerNiezaleznych.keys():
                    if not self.listaZerNiezaleznych[col] in listaOznakowanychWierszy:
                        tymczasowe_wiersze.append(self.listaZerNiezaleznych[col])
                        listaOznakowanychWierszy.append(self.listaZerNiezaleznych[col])

            kolumny_do_wykreslenia = self.wykreslKolumny(tymczasowe_wiersze, listaOznakowanychKolumn)
            listaOznakowanychKolumn.extend(kolumny_do_wykreslenia)

            if tymczasowe_wiersze:
                continue
            break

        #znajdz nieoznakowane wiersze
        listaNieOznakowanychWierszy = []
        for row_index in range(len(self.macierz)):
            if not row_index in listaOznakowanychWierszy:
                listaNieOznakowanychWierszy.append(row_index)

        self.wykresloneWiersze.extend(x for x in listaNieOznakowanychWierszy if x not in self.wykresloneWiersze)
        self.wykresloneKolumny.extend(x for x in listaOznakowanychKolumn if x not in self.wykresloneKolumny)

    def powiekszZbiorZerNiezaleznych(self):
        # tworzymy liste elementow macierzy bez elementow wykreslonych
        filtered_list = [self.macierz[i][j] for i in range(len(self.macierz)) for j in range(len(self.macierz[i])) \
                         if i not in self.wykresloneWiersze and j not in self.wykresloneKolumny]

        # znajdujemy najmniejszą wartość
        min_value = min(filtered_list)

        for rowIndex in range(len(self.macierz)):
            for colIndex in range(len(self.macierz[rowIndex])):
                if colIndex not in self.wykresloneKolumny and  rowIndex not in self.wykresloneWiersze:
                    self.macierz[rowIndex][colIndex] -= min_value
                elif colIndex in self.wykresloneKolumny and rowIndex in self.wykresloneWiersze:
                    self.macierz[rowIndex][colIndex] += min_value

        self.suma_redukcji_phi += min_value


    def wyznaczMacierzRozwiazania(self):
        rozmiar = len(self.macierz)
        rozwiazanie = np.zeros((rozmiar, rozmiar))

        for col in self.listaZerNiezaleznych:
            row = self.listaZerNiezaleznych[col]
            rozwiazanie[row][col] = 1

        return rozwiazanie


    def rozwiazanieAlgorytmu(self):

        while True:
            # krok 1. zredukuj macierz:
            self.matrix_redux()

            # krok 2. znajdz zera niezalezne:
            self.znajdzZeraNiezalezne()

            # sprawdz czy znaleziono rozwiazanie
            if len(self.listaZerNiezaleznych) == len(self.macierz):
                break

            # krok 3. wykreslanie wierszy i kolumn
            self.wykreslLinie()

            # sprawdz czy znaleziono rozwiazanie
            if len(self.wykresloneKolumny) + len(self.wykresloneWiersze) == len(self.macierz):
                break

            # krok 4. powieksz zbior zer niezaleznych
            self.powiekszZbiorZerNiezaleznych()

        print("wartosc funkcji kryterialnej: ", self.suma_redukcji_phi)
        print(self.wyznaczMacierzRozwiazania())

def main():
    # A = np.array([[5, 2, 3, 2, 7],
    #               [6, 8, 4, 2, 5],
    #               [6, 4, 3, 7, 2],
    #               [6, 9, 0, 4, 0],
    #               [4, 1, 2, 4, 0]])
    A = np.array([[3, 1, 3, 3, 3, 6],
                [6, 2, 2, 3, 2, 4],
                [7, 8, 9, 5, 6, 1],
                [3, 8, 5, 8, 7, 2],
                [9, 6, 1, 1, 6, 5],
                [9, 6, 1, 8, 9, 6]])
    # A = np.array([[8, 7, 9, 6, 8, 7],
    #              [2, 2, 2, 4, 7, 2],
    #              [4, 9, 5, 7, 5, 9],
    #              [1, 9, 2, 7, 4, 6],
    #              [4, 3, 1, 1, 7, 3],
    #              [1, 8, 4, 4, 1, 2]])
    Test = AlgorytmWegierski(A)
    Test.rozwiazanieAlgorytmu()


if __name__ == '__main__':
    main()







