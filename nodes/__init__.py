
from .models.mapa import *
from .models.structure import *
from .models.object import *
from .models.player import *
from .models.camera import *

from os import system

import time as tm

version: str = "1.1.12.23"

def _erase_screen():
    system("cls")

def start_game(player: Player,auto:bool = True, vec:list=[0,0]):
    
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

def queque():
    CUR[0].end = True
            
            