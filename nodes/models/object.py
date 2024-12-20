#Doc 1.0

from .obj.gen_obj import *

class Object(gen_obj):
    def __init__(self,
                 MAP,
                 X: int,
                 Y: int,
                 CHR: str,
                 NMO: str = "",
                 DATA: dict | list = ...):
        N_NUM[0] += 1
        super().__init__(X, Y, CHR, N_ABS[0], N_NUM[0], NMO)
        super().__map__(MAP)

        self.data = DATA

        self._set_meta("data", self.data)

    def set_data(self, nme: str, *arg):
        """
        Agrega/Edita nueva información a "data"
        """
        self.data[nme] = arg
        self._refresh_meta()

    def _refresh_meta(self):
        """
        actualiza el "meta" respecto a "data"
        """
        self._set_meta("data", self.data)

    def edit_data(self, nme_1: str, nme_2, arg):
        """
        edita información de "data"
        """
        if type(arg) == type([]) or type(arg) == type(()):
            if type(nme_2) != type(...):
                self.meta[nme_1][nme_2].append(arg)
            else:
                self.meta[nme_1].append(arg)
        else:
            self._set_meta(nme_1, arg)
        
        self._refresh_meta()

    def eraser_self(self):
        """
        El "object" se elimina asimismo del mapa
        """
        self.map.del_node(self)

