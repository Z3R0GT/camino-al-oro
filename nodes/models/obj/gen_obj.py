#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from .const.const import *

def _set_name(nme: str, nme_dft: tuple = ("DEFAULT", "NRO")):
    if type(nme) == type("n"):
        if nme != "":
            return nme
        else:
            return f"{nme_dft[0]}_{nme_dft[1]}"
    else:
        print(f"Nombre dado no es str, es: {type(nme)}")
        return "erno"

class gen_obj:

    def __init__(self,
                 X: int,
                 Y: int,
                 CHR: str,
                 ABS: str,
                 ID: int,
                 NMO: str):
        self.vec = [X, Y]
        self._temp_vec = [X, Y]

        self.abs = ABS
        self.id = ID

        self.character = CHR
        self.name = _set_name(NMO, (self.abs, self.id))

        self.meta = {
            "name": self.name,
            "vec": self.vec,
            "abs": self.abs,
            "id": self.id,
            "chr": self.character
        }

    def __transform__(self, size_x, size_y):
        self.transform = (size_x, size_y)
        self._set_meta("transform", self.transform)

    def __map__(self, MAP):
        self.map = MAP
        self._set_meta("map", (self.map.id, self.map.name))
        
    #####################################################
    #                      META ZONE                    #
    #####################################################
    def _set_meta(self, nme: str, arg):
        self.meta[nme] = arg

    def _edit_meta(self, nme_1: str, nme_2, arg):
        if type(arg) == type([]) or type(arg) == type(()):
            if type(nme_2) != type(...):
                self.meta[nme_1][nme_2].append(arg)
            else:
                self.meta[nme_1].append(arg)
        else:
            self._set_meta(nme_1, arg)

    def get_meta(self):
        return self.meta

    #####################################################
    #                      FUNC ZONE                    #
    #####################################################

    def _insert(self, old_, new_, from_=..., to_=..., specific_=...) -> str:
        """
        inserta una cadena de texto y retorna una nueva desde unas coordenas o en especifico uno

        :param old_: vieja cadena
        :param new_: nueva cadena
        :param from_: empieza a insertar
        :param to_: termina de insertar
        :param specific_: coordenada especifica
        :return: str
        """
        temp = []
        new = ""
        cont = 0

        for i in range(len(old_)):
            temp.append(old_[i])

        if to_ is ... and from_ is not ...:
            to_ = len(new_) + from_

        for mw in range(len(temp)):
            if specific_ is not ...:
                if mw > 0 and mw == specific_:
                    temp[mw] = new_
            elif mw in range(from_, to_):
                temp[mw] = new_[cont]
                cont += 1

        for i in range(len(temp)):
            new += temp[i]

        return new
