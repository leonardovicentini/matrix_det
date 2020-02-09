#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Vicentini Leonardo"
__version__ = "01_01"


import os
import argparse
from functools import wraps
from tabulate import tabulate


boold = False


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
        return tabulate(self.grid, tablefmt="grid")

    def __repr__(self):
        string = ""
        for i in range(0, self.ord):
            string += str(self.grid[i]) + "\n"
        return string

    @function_debugger
    def undermatrix(self, line, column):
        """
        Crea una sottomatrice a partire da quella di partenza eliminando la riga e la colonna indicata.
        :param line: int Indice della linea da eliminare.
        :param column: int Indice della colonna da eliminare.
        :return: Matrix Sottomatrice di quella di partenza.
        """
        undermatrix = Matrix(self.ord - 1)
        undermatrix.grid = []

        for subline in self.grid:
            undermatrix.grid.append(subline.copy())

        del undermatrix.grid[line]
        
        for i in range(0, undermatrix.ord):
            del undermatrix.grid[i][column]

        if boold or verbose: print("Undermatrix:\n", undermatrix, sep="")

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

    if boold or verbose: print(f"Det = {determinante}")

    return determinante


@function_debugger
def det(matrix):
    """
    Data una matrice ne calcola dil determinante.
    :param matrix: Matrix Matrice di cui calcloare il determinante.
    :return: float Determinante della matrice
    """
    if matrix.ord == 2:
        return det_ord2(matrix)
    else:
        determinante = 0
        i = 0
        for j in range(0, matrix.ord):
            determinante += ((-1) ** (i + j)) * matrix.grid[i][j] * det(matrix.undermatrix(i,j))
        
        return determinante


@function_debugger
def get_order(arg):
    """
    Restituisce l'ordine della matrice da costruire.
    :param arg: int Argomento passato al parametro opzionale -o
    :return: int Ordine della matrice.
    """
    order = 0
    if arg:
        order = arg
    else:
        valid_input = False
        while not valid_input:
            try:
                order = int(input("Insert matrix order: "))
                if order < 2: print("Invalid int value.")  
                else: valid_input = True

            except ValueError:
                print("Invalid int value.")

    return order


@function_debugger
def check_file_matrix(file_path):
    """
    Verifica che il file in ingresso sia adatto all'elaborazione.
    :param file_path: str Percorso del file .csv
    :return: bool True se adatto, False se non adatto.
    """
    check = True

    with open(file_path, "r") as matrix_file:
        lines = matrix_file.readlines()
        column = len(lines)
        
        for line in lines:
            values = line.strip("\n").split(";")
            if len(values) != len(lines):
                check = False
            
            for value in values:
                try:
                    float(value)
                except ValueError:
                    check = False

    return check


@function_debugger
def matrix_from_file(file):
    """
    Ritorna una matrice da un file csv
    :param file: str Percorso del file .csv
    :return Matrix Matrice che contiene i valori del file .csv
    """
    if not check_file_matrix(file):
        print("Wrong format.")
    else:
        with open(file, "r") as matrix_file:
            lines = matrix_file.readlines()
            order = len(lines)
            matrix = Matrix(order)

            for i in range(0, len(lines)):
                str_line = lines[i].split(";")
                float_line = [float(value) for value in str_line]

                for value in float_line:
                    if boold: print(f"{value} added.")
                    matrix.grid[i].append(value)
        
        return matrix


@function_debugger
def matrix_from_input():
    """
    Ottiene la matrice da input.
    :return: Matrix Matrice creata.
    """
    ord = get_order(args.ord)

    matrix = Matrix(ord)
    valid_input = False

    if boold: print(matrix)

    for i in range(0, matrix.ord):
        for j in range(0, matrix.ord):
            while not valid_input:
                try:
                    value = float(input(f"Insert value in position({i+1},{j+1}): "))
                    valid_input = True
                    matrix.grid[i].append(value)
                except ValueError:
                    print("Wrong input.")
                    valid_input = False
            valid_input = False

    return matrix


if __name__ == "__main__":

    if boold: print("Start main")

    parser = argparse.ArgumentParser(description="Programma per il calcolo del determinante di una matrice.", prog="matrix_det")
    parser.add_argument("-v", "--verbose", help="Output verboso.", action="store_true")
    parser.add_argument("--version", help="show program version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-o", "--ord", help="Specificare l'ordine della matrice dalla cli.", type=int)
    parser.add_argument("-f", "--file", help="Importare la matrice da un file .csv", type=str)

    args = parser.parse_args()

    verbose = args.verbose

    if args.file:
        matrix = matrix_from_file(args.file)
    
    else:
        matrix = matrix_from_input()


    if type(matrix) == type(Matrix(1)):
        print(matrix)

        print("Det =", det(matrix))

    if boold: print("End main")
