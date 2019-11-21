#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Vicentini Leonardo"
__version__ = "01_01"


import os
import sys
from functools import wraps


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


@function_debugger
def check_params():
    """
    Gestione dei parametri per ottenere la stringa e la cartella 
    contenente i file su cui operare.
    :return string: str Stringa da cercare.
    :return folder: str Percorso della cartella in cui cercare.
    """
    parametri = sys.argv[1:]
    if len(parametri) != 2:
        print("Errato numero di parametri."); exit(-1)
    else:
        if not os.path.isdir(parametri[1]):
            print(f"La cartella , {parametri[1]} non esistente"); exit(-1)

    return parametri


if __name__ == "__main__":

    if boold:
        print("Start main")

    stringa, cartella = check_params()

    if boold: print(f"Parametri: {stringa} {cartella}")

    for root, dirs, files in os.walk(cartella):
        for file in files:
            if file.endswith(".log"):
                file = os.path.join(root, file)
                with open(file, "r") as log_file:
                    linea = 1
                    for line in log_file:
                        if stringa in line:
                            print(f"Stringa '{stringa}' nel file '{file}' alla riga {linea}.")
                        linea += 1

    if boold:
        print("End main")
