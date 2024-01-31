#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from nodes.models.const import const as const

from nodes.models.obj.gen_obj import *


class Object(gen_obj):

    def __init__(self,
                 MAP,
                 X: int,
                 Y: int,
                 CHR: str,
                 NMO: str = "",
                 DATA: dict | list = ...):
        const.obj += 1

        super().__init__(X, Y, CHR, const.n_abs[0], const.obj, NMO)
        super().__map__(MAP)


        self.data = DATA

        self._set_meta("data", self.data)

    def set_data(self, nme: str, *arg):
        self.data[nme] = arg

    def edit_data(self, nme_1: str, nme_2, arg):
        if type(arg) == type([]) or type(arg) == type(()):
            if type(nme_2) != type(...):
                self.meta[nme_1][nme_2].append(arg)
            else:
                self.meta[nme_1].append(arg)
        else:
            self._set_meta(nme_1, arg)

    def eraser_self(self):
        self.map.del_node(self)

