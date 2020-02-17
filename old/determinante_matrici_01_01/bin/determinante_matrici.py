# -*- coding: utf-8 -*-

__author__ = "Vicentini Leonardo"
__version__ = "01.01"


import os


boold = False


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

    ordine = 2
    matrice = []

    e11 = float(input("Inserire l'elemento di posto 1,1: "))
    e12 = float(input("Inserire l'elemento di posto 1,2: "))
    e21 = float(input("Inserire l'elemento di posto 2,1: "))
    e22 = float(input("Inserire l'elemento di posto 2,2: "))

    matrice = [[e11, e12],
                [e21, e22]]

    det = determinante_matrice_ordine2(matrice)

    print(f"Il determinante della matrice \n"
                f"{matrice[0]} \n"
                f"{matrice[1]} \n"
                f"vale: {det}")


    if boold:
        print("End")
