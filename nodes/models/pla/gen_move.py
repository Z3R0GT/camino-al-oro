#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import pprint
import time as tn

class gen_move():
    
    def __coords__(self):
        self.global_x = self.vec[0]
        self.global_y = self.vec[1]

    def _zero_in(self):
        self.__in_x = 0
        self.__in_y = 0

    def _check_nxt_foot(self, coll: list) -> tuple:
        """
        Verifica si el siguiente movmiento no tiene un caracter de colision, sean
        True || False los indicadores
        :return: True || False
        """
        self.lim = (self.map.vec[0], self.map.vec[1])

        if len(coll) == 0:
            return False, ""

        x = self.__in_x
        y = self.__in_y

        for collision in coll:
            # Verifica que las cordenas no pasen el limite
            if (self.global_x + x != self.lim[0] and self.global_x + x < self.lim[0]) and (
                    self.global_y + y != self.lim[1] and self.global_y + y < self.lim[1]):
                
                if x != 0:
                    if self.map.square[self.global_y][self.global_x + x] == collision:
                        return False, collision
                    return True, collision
                elif y != 0:
                    if self.map.square[self.global_y + y][self.global_x] == collision:
                        return False, collision
                    return True, collision
            else:
                print("Limite excedido")
                return False, collision

    def __obj_take(self):
        chr_obj = []
        nme_obj = []
        dat_obj = []

        obj_lst = self.map.meta["node_lst"]["obj"]
        for lst in range(len(obj_lst)):
            chr_obj.append(obj_lst[lst]["chr"])
            nme_obj.append(obj_lst[lst]["name"])
            dat_obj.append(obj_lst[lst]["data"])

        return chr_obj, nme_obj, dat_obj

    def _move_body(self, in_):
        if self.map.pause:
            return

        self._zero_in()
        w, s, a, d = self.controll

        if in_ == w:
            self.__in_y = -1
        elif in_ == s:
            self.__in_y = 1
        elif in_ == a:
            self.__in_x = -1
        elif in_ == d:
            self.__in_x = 1

        self.input = (self.__in_x, self.__in_y)

        if self._check_nxt_foot(self.coll)[0]:
            temp = self.__obj_take()
            check = self._check_nxt_foot(temp[0])
            if not check[0]:
                n = 0
                for i in temp[0]:
                    n += 1
                    if i == check[1]:
                        try:
                            if self.inv[temp[1][n-1]]:
                              self.inv[temp[1][n-1]][0] += 1
                        except KeyError:
                            self.inv[temp[1][n-1]] = [0, temp[2][n-1]]
                        finally:
                            break

            self._appear_map()

        #if self.cifs:
        #self.some_info()
        
        #self._zero_in()

