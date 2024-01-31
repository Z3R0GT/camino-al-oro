#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from nodes.models.map import *
from nodes.models.structure import *
from nodes.models.object import *
from nodes.models.player import *
from nodes.models.camera import *
from nodes.models.window import *

version: str = "1.1.12.23"

def start_game(main_map: Map):
    X_cols = main_map.vec[0]+30
    Y_lins = main_map.vec[1]+5

    from os import system    
    system(f'mode con: cols={X_cols} lines={Y_lins}')
    
    main_map.get_pre_view()