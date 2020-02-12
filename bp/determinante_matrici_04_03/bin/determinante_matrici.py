# -*- coding: utf-8 -*-

__author__ = "Vicentini Leonardo"
__version__ = "04.01"


import os


boold = False


def determinante_matrice_ordine5(matrice_o5):
    """
    Questa funzione, data una matrice quadrata di ordine 5 restituisce il suo determinante.
    :param matrice_o5: list, martice di ordine 5 di cui si vuole calcolare i determinante.
    :return: int, determinante della matrice.
    """

    if boold:
        print("Start funzione determinante_matrice_ordine5(matrice_o5)")

    prima_sottomatrice = [[matrice_o5[1][1], matrice_o5[1][2], matrice_o5[1][3], matrice[1][4]],
                          [matrice_o5[2][1], matrice_o5[2][2], matrice_o5[2][3], matrice[2][4]],
                          [matrice_o5[3][1], matrice_o5[3][2], matrice_o5[3][3], matrice[3][4]],
                          [matrice_o5[4][1], matrice_o5[4][2], matrice_o5[4][3], matrice[4][4]]]

    seconda_sottomatrice = [[matrice_o5[1][0], matrice_o5[1][2], matrice_o5[1][3], matrice[1][4]],
                            [matrice_o5[2][0], matrice_o5[2][2], matrice_o5[2][3], matrice[2][4]],
                            [matrice_o5[3][0], matrice_o5[3][2], matrice_o5[3][3], matrice[3][4]],
                            [matrice_o5[4][0], matrice_o5[4][2], matrice_o5[4][3], matrice[4][4]]]

    terza_sottomatrice = [[matrice_o5[1][0], matrice_o5[1][1], matrice_o5[1][3], matrice[1][4]],
                          [matrice_o5[2][0], matrice_o5[2][1], matrice_o5[2][3], matrice[2][4]],
                          [matrice_o5[3][0], matrice_o5[3][1], matrice_o5[3][3], matrice[3][4]],
                          [matrice_o5[4][0], matrice_o5[4][1], matrice_o5[4][3], matrice[4][4]]]

    quarta_sottomatrice = [[matrice_o5[1][0], matrice_o5[1][1], matrice_o5[1][2], matrice[1][4]],
                           [matrice_o5[2][0], matrice_o5[2][1], matrice_o5[2][2], matrice[2][4]],
                           [matrice_o5[3][0], matrice_o5[3][1], matrice_o5[3][2], matrice[3][4]],
                           [matrice_o5[4][0], matrice_o5[4][1], matrice_o5[4][2], matrice[4][4]]]

    quinta_sottomatrice = [[matrice_o5[1][0], matrice_o5[1][1], matrice_o5[1][2], matrice[1][3]],
                           [matrice_o5[2][0], matrice_o5[2][1], matrice_o5[2][2], matrice[2][3]],
                           [matrice_o5[3][0], matrice_o5[3][1], matrice_o5[3][2], matrice[3][3]],
                           [matrice_o5[4][0], matrice_o5[4][1], matrice_o5[4][2], matrice[4][3]]]

    primo_complemento_algebrico = 1 * determinante_matrice_ordine4(prima_sottomatrice)
    secondo_complemento_algebrico = -1 * determinante_matrice_ordine4(seconda_sottomatrice)
    terzo_complemento_algebrico = 1 * determinante_matrice_ordine4(terza_sottomatrice)
    quarto_complemento_algebrico = -1 * determinante_matrice_ordine4(quarta_sottomatrice)
    quinto_complemento_algebrico = 1 * determinante_matrice_ordine4(quinta_sottomatrice)

    primo_prodotto = matrice_o5[0][0] * primo_complemento_algebrico
    secondo_prodotto = matrice_o5[0][1] * secondo_complemento_algebrico
    terzo_prodotto = matrice_o5[0][2] * terzo_complemento_algebrico
    quarto_prodotto = matrice_o5[0][3] * quarto_complemento_algebrico
    quinto_prodotto = matrice_o5[0][4] * quinto_complemento_algebrico

    determinante = primo_prodotto + secondo_prodotto + terzo_prodotto + quarto_prodotto

    if boold:
        print(f"  Elementi dati: \n"
              f"  {matrice_o5[0]} \n"
              f"  {matrice_o5[1]} \n"
              f"  {matrice_o5[2]} \n"
              f"  {matrice_o5[3]} \n"
              f"  {matrice_o5[4]}")
        print(f"  Calcolo: {primo_prodotto} + {secondo_prodotto} + {terzo_prodotto} +"
              f" {quarto_prodotto} + {quinto_prodotto} = {determinante}")
        print("End funzione determinante_matrice_ordine5(matrice_o5)")

    return determinante


def determinante_matrice_ordine4(matrice_o4):
    """
    Questa funzione, data una matrice quadrata di ordine 4 restituisce il suo determinante.
    :param matrice_o4: list, martice di ordine 4 di cui si vuole calcolare i determinante.
    :return: int, determinante della matrice.
    """

    if boold:
        print("Start funzione determinante_matrice_ordine4(matrice_o4)")

    prima_sottomatrice = [[matrice_o4[1][1], matrice_o4[1][2], matrice_o4[1][3]],
                          [matrice_o4[2][1], matrice_o4[2][2], matrice_o4[2][3]],
                          [matrice_o4[3][1], matrice_o4[3][2], matrice_o4[3][3]]]

    seconda_sottomatrice = [[matrice_o4[1][0], matrice_o4[1][2], matrice_o4[1][3]],
                            [matrice_o4[2][0], matrice_o4[2][2], matrice_o4[2][3]],
                            [matrice_o4[3][0], matrice_o4[3][2], matrice_o4[3][3]]]

    terza_sottomatrice = [[matrice_o4[1][0], matrice_o4[1][1], matrice_o4[1][3]],
                          [matrice_o4[2][0], matrice_o4[2][1], matrice_o4[2][3]],
                          [matrice_o4[3][0], matrice_o4[3][1], matrice_o4[3][3]]]

    quarta_sottomatrice = [[matrice_o4[1][0], matrice_o4[1][2], matrice_o4[1][2]],
                           [matrice_o4[2][0], matrice_o4[2][2], matrice_o4[2][2]],
                           [matrice_o4[3][0], matrice_o4[3][2], matrice_o4[3][2]]]

    primo_complemento_algebrico = 1 * determinante_matrice_ordine3(prima_sottomatrice)
    secondo_complemento_algebrico = -1 * determinante_matrice_ordine3(seconda_sottomatrice)
    terzo_complemento_algebrico = 1 * determinante_matrice_ordine3(terza_sottomatrice)
    quarto_complemento_algebrico = -1 * determinante_matrice_ordine3(quarta_sottomatrice)

    primo_prodotto = matrice_o4[0][0] * primo_complemento_algebrico
    secondo_prodotto = matrice_o4[0][1] * secondo_complemento_algebrico
    terzo_prodotto = matrice_o4[0][2] * terzo_complemento_algebrico
    quarto_prodotto = matrice_o4[0][3] * quarto_complemento_algebrico

    determinante = primo_prodotto + secondo_prodotto + terzo_prodotto + quarto_prodotto

    if boold:
        print(f"  Elementi dati: \n"
              f"  {matrice_o4[0]} \n"
              f"  {matrice_o4[1]} \n"
              f"  {matrice_o4[2]} \n"
              f"  {matrice_o4[3]}")
        print(f"  Calcolo: {primo_prodotto} + {secondo_prodotto} + {terzo_prodotto} + {quarto_prodotto}"
              f" = {determinante}")
        print("End funzione determinante_matrice_ordine4(matrice_o4)")

    return determinante


def determinante_matrice_ordine3(matrice_o3):
    """
    Questa funzione, data una matrice quadrata di ordine 3 restituisce il suo determinante.
    :param matrice_o3: list, martice di ordine 3 di cui si vuole calcolare i determinante.
    :return: int, determinante della matrice.
    """
    if boold:
        print("Start funzione determinante_matrice_ordine3(matrice_o3)")

    prima_sottomatrice = [[matrice_o3[1][1], matrice_o3[1][2]],
                          [matrice_o3[2][1], matrice_o3[2][2]]]

    seconda_sottomatrice = [[matrice_o3[1][0], matrice_o3[1][2]],
                            [matrice_o3[2][0], matrice_o3[2][2]]]

    terza_sottomatrice = [[matrice_o3[1][0], matrice_o3[1][1]],
                          [matrice_o3[2][0], matrice_o3[2][1]]]

    primo_complemento_algebrico = 1 * determinante_matrice_ordine2(prima_sottomatrice)
    secondo_complemento_algebrico = -1 * determinante_matrice_ordine2(seconda_sottomatrice)
    terzo_complemento_algebrico = 1 * determinante_matrice_ordine2(terza_sottomatrice)

    primo_prodotto = matrice_o3[0][0] * primo_complemento_algebrico
    secondo_prodotto = matrice_o3[0][1] * secondo_complemento_algebrico
    terzo_prodotto = matrice_o3[0][2] * terzo_complemento_algebrico

    determinante = primo_prodotto + secondo_prodotto + terzo_prodotto

    if boold:
        print(f"  Elementi dati: \n"
              f"  {matrice_o3[0]} \n"
              f"  {matrice_o3[1]} \n"
              f"  {matrice_o3[2]}")
        print(f"  Calcolo: {primo_prodotto} + {secondo_prodotto} + {terzo_prodotto} = {determinante}")
        print("End funzione determinante_matrice_ordine3(matrice_o3)")

    return determinante


def determinante_matrice_ordine2(matrice_o2):
    """
    Questa funzione, data una matrice quadrata di ordine 2 restituisce il suo determinante.
    :param matrice_o2: list, martice di ordine 2 di cui si vuole calcolare i determinante.
    :return: int, determinante della matrice
    """

    if boold:
        print("Start funzione determinante_matrice_ordine2(matrice_o2)")

    primo_prodotto = matrice_o2[0][0] * matrice_o2[1][1]
    secondo_prodotto = matrice_o2[0][1] * matrice_o2[1][0]

    determinante = primo_prodotto - secondo_prodotto

    if boold:
        print(f"  Elementi dati: \n"
              f"  {matrice_o2[0]} \n"
              f"  {matrice_o2[1]}")
        print(f"  Calcolo: {primo_prodotto} - {secondo_prodotto} = {determinante}")
        print(f"  Determinante = {determinante}")
        print("End funzione determinante_matrice_ordine2(matrice_o2)")

    return determinante


if __name__ == "__main__":

    if boold:
        print("Start")

    ordine = 0
    matrice = []
    e11 = ""
    e12 = ""
    e13 = ""
    e14 = ""
    e15 = ""
    e21 = ""
    e22 = ""
    e23 = ""
    e24 = ""
    e25 = ""
    e31 = ""
    e32 = ""
    e33 = ""
    e34 = ""
    e35 = ""
    e41 = ""
    e42 = ""
    e43 = ""
    e44 = ""
    e45 = ""
    e51 = ""
    e52 = ""
    e53 = ""
    e54 = ""
    e55 = ""

    try:
        ordine = int(input("Inserire l'ordine della matrice (min 2, max 5): "))
        if ordine < 2 or ordine > 5:
            print("Ordine inserito non valido")
            exit(-1)

        # Prima riga
        e11 = float(input("Inserire l'elemento di posto 1,1: "))
        e12 = float(input("Inserire l'elemento di posto 1,2: "))
        if ordine >= 3:
            e13 = float(input("Inserire l'elemento di posto 1,3: "))
            if ordine >= 4:
                e14 = float(input("Inserire l'elemento di posto 1,4: "))
                if ordine == 5:
                    e15 = float(input("Inserire l'elemento di posto 1,5: "))

        # Seconda riga
        e21 = float(input("Inserire l'elemento di posto 2,1: "))
        e22 = float(input("Inserire l'elemento di posto 2,2: "))
        if ordine >= 3:
            e23 = float(input("Inserire l'elemento di posto 2,3: "))
            if ordine >= 4:
                e24 = float(input("Inserire l'elemento di posto 2,4: "))
                if ordine == 5:
                    e25 = float(input("Inserire l'elemento di posto 2,5: "))

        # Terza riga
        if ordine >= 3:
            e31 = float(input("Inserire l'elemento di posto 3,1: "))
            e32 = float(input("Inserire l'elemento di posto 3,2: "))
            e33 = float(input("Inserire l'elemento di posto 3,3: "))
            if ordine >= 4:
                e34 = float(input("Inserire l'elemento di posto 3,4: "))
                if ordine == 5:
                    e35 = float(input("Inserire l'elemento di posto 3,5: "))

        # Quarta riga
        if ordine >= 4:
            e41 = float(input("Inserire l'elemento di posto 4,1: "))
            e42 = float(input("Inserire l'elemento di posto 4,2: "))
            e43 = float(input("Inserire l'elemento di posto 4,3: "))
            e44 = float(input("Inserire l'elemento di posto 4,4: "))
            if ordine == 5:
                e45 = float(input("Inserire l'elemento di posto 4,5: "))

        # Quinta riga
        if ordine == 5:
            e51 = float(input("Inserire l'elemento di posto 5,1: "))
            e52 = float(input("Inserire l'elemento di posto 5,2: "))
            e53 = float(input("Inserire l'elemento di posto 5,3: "))
            e54 = float(input("Inserire l'elemento di posto 5,4: "))
            e55 = float(input("Inserire l'elemento di posto 5,5: "))

        # creazione matrice
        if ordine == 2:
            matrice = [[e11, e12],
                       [e21, e22]]
            det = determinante_matrice_ordine2(matrice)

            print(f"Il determinante della matrice \n"
                  f"{matrice[0]} \n"
                  f"{matrice[1]} \n"
                  f"vale: {det}")

        elif ordine == 3:
            matrice = [[e11, e12, e13],
                       [e21, e22, e23],
                       [e31, e32, e33]]
            det = determinante_matrice_ordine3(matrice)

            print(f"Il determinante della matrice: \n"
                  f"{matrice[0]} \n"
                  f"{matrice[1]} \n"
                  f"{matrice[2]} \n"
                  f"vale: {det}")

        elif ordine == 4:
            matrice = [[e11, e12, e13, e14],
                       [e21, e22, e23, e24],
                       [e31, e32, e33, e34],
                       [e41, e42, e43, e44]]
            det = determinante_matrice_ordine4(matrice)

            print(f"Il determinante della matrice: \n"
                  f"{matrice[0]} \n"
                  f"{matrice[1]} \n"
                  f"{matrice[2]} \n"
                  f"{matrice[3]} \n"
                  f"vale: {det}")

        elif ordine == 5:
            matrice = [[e11, e12, e13, e14, e15],
                       [e21, e22, e23, e24, e25],
                       [e31, e32, e33, e34, e35],
                       [e41, e42, e43, e44, e45],
                       [e15, e25, e35, e45, e45]]
            det = determinante_matrice_ordine5(matrice)

            print(f"Il determinante della matrice: \n"
                  f"{matrice[0]} \n"
                  f"{matrice[1]} \n"
                  f"{matrice[2]} \n"
                  f"{matrice[3]} \n"
                  f"{matrice[4]} \n"
                  f"vale: {det}")

    except ValueError:
        print("Valore inserito non valido")

    if boold:
        print("End")
