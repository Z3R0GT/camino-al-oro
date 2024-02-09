#Doc 1.0

from .models.mapa import *
from .models.structure import *
from .models.object import *
from .models.player import *
from .models.camera import *
from .models.page import *

from os import system

import time as tm

version: str = "1.2.12.23"
"""
version de la libreria, siendo:
{n lanzamiento}.{n update}.{mes}.{año}
"""

def _erase_screen():
    """
    Limpia la consola
    """
    system("cls")

def start_game(player: Player,auto:bool = True, vec:list=[0,0]):
    """
    requiere del jugador y que previamente actualizaras el mapa y la camara.
    
    puedes dejar que el tamaño de la ventana sea automatica (toma referencia del mapa)
    o cambiar el estado de "auto" y con "vec" colocar las que quieras
    """
    
    try:
        if auto: 
            X_cols = CUR[0].vec[0]+30
            Y_lins = CUR[0].vec[1]+5
        else:
            X_cols = vec[0]
            Y_lins = vec[1]

        from os import system    
        system(f'mode con: cols={X_cols} lines={Y_lins}')
    
        player.move()
    
        while not CUR[0].end:
            if not CUR[0].pause:
                CUR[1].render_image()
            
                _erase_screen()
            
                CUR[1].get_pre_view()
                tm.sleep(N_FP[2])
        
            if CUR[0].end:
                break
    except Exception as e:
        print(f"Frame de error:{N_FP[1]} + error: {e} ")

def queque():
    """
    Termina el programa
    """
    CUR[0].end = True
            
            
