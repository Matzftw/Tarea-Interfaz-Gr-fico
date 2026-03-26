
"""Tarea 1 Progra Max Q.H"""

import tkinter as tk
import math as mt   #import super util (no hizo nada)
import pygame #Solo para audio
from PIL import Image #Solo para imagenes


def pares(num):
    if num == 0:
        return (0,0)
    elif isinstance(num,int) and num > 0 and num < 9999:
        return pares_aux(abs(num))
    else:
        return -1

def pares_aux(num):
    if num == 0:
        b = num // a
        if a <= b:
            return ({a}, {b})
    else:
        return -1

