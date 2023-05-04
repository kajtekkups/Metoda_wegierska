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
                        self.listaKolumnZerNiezaleznych.append(zeroColIndex)
                        self.listaWierszyZerNiezaleznych.append(zeroRowIndex)
                        self.listaZerNiezaleznych[zeroColIndex] = zeroRowIndex
                    else:
                        self.listaKolumnZeZaleznych.append(zeroColIndex)


    def sprawdzCzyNiezalezne(self, elementRow, elementCol):
        #sprawdz czy w wierszu jest juz zero
        if elementRow in self.listaWierszyZerNiezaleznych:
            return False

        #sprawdz czy w kolumnie jest juz zero
        if elementCol in self.listaKolumnZerNiezaleznych:
            return False

        return True



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
    A = np.array([[5, 2, 3, 2, 7],
                  [6, 8, 4, 2, 5],
                  [6, 4, 3, 7, 2],
                  [6, 9, 0, 4, 0],
                  [4, 1, 2, 4, 0]])

    Test = AlgorytmWegierski(A)
    Test.rozwiazanieAlgorytmu()


if __name__ == '__main__':
    main()







