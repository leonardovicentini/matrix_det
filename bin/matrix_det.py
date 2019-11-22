#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Vicentini Leonardo"
__version__ = "01_01"


import os
from functools import wraps


boold = True



def function_debugger(function):
    function_debugger.__author__ = "Vicentini Leonardo"
    """
    Decoratore a scopo di debugging per le funzioni. Compariranno messaggi
    'Start' e 'End' al fine di analizzare il comportamento dello script.
    Si presume l'esistenza della variabile globale 'boold' e dell'importazione
    di 'wraps' dal modulo della Standard Library 'functools'.
    Happy debugging! :-)
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        if boold: print(f"Start {function.__name__}()")
        return_value = function(*args, **kwargs)
        if boold: print(f"End {function.__name__}()")
        return return_value

    return wrapper


class Matrix:

    @function_debugger
    def __init__(self, ord):
        self.grid = []
        for i in range(0, ord):
            self.grid.append([])
        self.ord = ord

    def __str__(self):
        string = ""
        for i in range(0, self.ord):
            string += str(self.grid[i]) + "\n"
        return string

    @function_debugger
    def undermatrix(self, line, column):
        """
        """
        undermatrix = Matrix(self.ord - 1)
        undermatrix.grid = self.grid[:]

        del undermatrix.grid[line]
        
        for i in range(0, undermatrix.ord):
            #print("sottomatrice:\n",undermatrix,"matrice\n", self, sep = "")
            print(undermatrix.grid[i][column] is self.grid[i][column])
            del undermatrix.grid[i][column]
        
        if boold: print("Sottomatrice:\n", undermatrix, sep="")

        return undermatrix


@function_debugger
def det_ord2(matrix_ord2):
    """
    Questa funzione, data una matrice quadrata di ordine 2 restituisce il suo determinante.
    :param matrice_o2: list, martice di ordine 2 di cui si vuole calcolare i determinante.
    :return: int, determinante della matrice
    """
    primo_prodotto = matrix_ord2.grid[0][0] * matrix_ord2.grid[1][1]
    secondo_prodotto = matrix_ord2.grid[0][1] * matrix_ord2.grid[1][0]
    determinante = primo_prodotto - secondo_prodotto

    print(f"Determinante di:\n{matrix_ord2}\n= {determinante}")

    return determinante


@function_debugger
def det(matrix):
    if matrix.ord == 2:
        return det_ord2(matrix)
    else:
        determinante = 0
        i = 0
        for j in range(0, matrix.ord):
            determinante += ((-1) ** (i + j)) * matrix.grid[i][j] * det(matrix.undermatrix(i,j))
            print("Matrice di partenza: \n", matrix, sep="")
            print("Determinante: ", determinante)
        return determinante


if __name__ == "__main__":

    if boold:
        print("Start main")

    ord = 3

    matrix = Matrix(ord)

    if boold: print(matrix)

    for i in range(0, matrix.ord):
        for j in range(0, matrix.ord):
            value = int(input(f"Insert value in position({i},{j}): "))
            matrix.grid[i].append(value)

    if boold: print(matrix)

    #print(det(matrix))

    matrix.undermatrix(2, 2)

    print(matrix)

    if boold:
        print("End main")
