#Doc V 1.0

import pynput as pn

from .pla.gen_pla import *
from .pla.gen_move import *

from .obj.gen_obj import *


class Player(gen_obj, gen_pla, gen_move):

    def __init__(self,
                 MAP,
                 X: int,
                 Y: int,
                 CHR: str,
                 EXPT_COLL: list = ...,
                 NMO: str = "",
                 CONTROLLS: list = ["w", "s", "a", "d"],
                 CIFS: bool = False):
        N_NUM[1] += 1
        super().__init__(X, Y, CHR, N_ABS[2], N_NUM[1], NMO)
        super().__map__(MAP)
        
        self.__coords__()
        self.__start__(EXPT_COLL, CONTROLLS, CIFS)

        self.inv = {}
        self.key = pn.keyboard

        self._set_meta("inv", self.inv)

    def __on_press(self, key):
        """
        cuando la tecla es presionada, sumara o actualizara sea
        .__in_x y .__in_y las entrada
        """
        try:
            self._move_body(key.char)
        except AttributeError:
            # Caracteres especiales (ESC, SPACE)
            if key == pn.keyboard.Key.esc:
                self.map.end = True
            elif key == pn.keyboard.Key.space:
                if not self.map.pause:
                    self.map.pause = True
                else:
                    self.map.pause = False

    def __on_realease(self, key):
        """
        Cuando la tecla dejo de ser presionada
        """
        if key == pn.keyboard.Key.esc:
            return False

    def move(self):
        """
        comienza a capturar el moviento de teclado en todo momento 
        hasta el final de la ejecución
        """
        lst = self.key.Listener(on_press=self.__on_press, on_release=self.__on_realease)
        lst.start()
# crear en meta un "inv" que contendra los N objetos (que sea diccionario)
