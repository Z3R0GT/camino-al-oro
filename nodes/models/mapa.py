#Doc 1.0

from .wns.gen_wns import *
from .obj.gen_obj import *

class Mapa(gen_obj, gen_wns):
    def __init__(self,
                 X: int,
                 Y: int,
                 CHR: str,
                 NMO: str = ""):
        N_NUM[2] += 1
        super().__init__(X, Y, CHR, N_ABS[4], N_NUM[2], NMO)
        super().__wns__()

        self.end = False
        self.pause = False

        self.coll = []

        self.node_list = {
            "obj": [],
            "cam": [],
            "pla": [],
            "npc": [],
            "stu": []
        }

        self._set_meta("end", self.end)
        self._set_meta("pause", self.pause)

        self._set_meta("coll", self.coll)

        self._set_meta("node_lst", self.node_list)

        self._create_square(self.vec)
        self._create_ln_low_num(self.vec[0])
        self._create_pre_view()

    def _check_own(self, node) -> bool:
        """
        Verifica si el objeto fue creado para este mapa
        """
        return self.id != node.meta["map"][0]

    def erase_coll(self, obj):
        """
        Elimina una colición con base al objeto
        """
        if self._check_own(obj):
            return

        c = 0
        for coll in self.coll:
            c += 1
            if coll == obj.character:
                self.coll[c - 1] = f"{obj.abs}_{obj.id}"
        self._set_meta("coll", self.coll)

    def set_coll(self, obj):
        """
        Agrega una colisión con base al objeto
        """
        if self._check_own(obj):
            return

        c = 0
        for coll in self.coll:
            c += 1
            if len(coll) > 1:

                if coll[0:3] == obj.abs and coll[4] == obj.id:
                    self.coll[c - 1] = obj.character

        if obj.character not in self.coll:
            self.coll.append(obj.character)

        self._set_meta("coll", self.coll)

    def add_node(self, node, exception:bool=False):
        """
        Agrega un objeto/nodo, dependiendo del abecedario con el que fue creado
        """
        if self._check_own(node):
            return print(f"{node.name} no pertenece a {self.name}")

        if node.abs == "stu":
            if self.vec[0] < node.vec[0] or self.vec[1] < node.vec[1]:
                return print("Nodo excede los limites")

            c = 0
            for y in range(self.vec[1]):
                if y in range(node.vec[1], (node.vec[1] + node.transform[1])):
                    c += 1
                    for x in range(self.vec[0]):
                        if x in range(node.vec[0], (node.vec[0] + node.transform[0])):
                            self.square[y] = self._insert(
                                self.square[y],
                                node.square[(c - 1)],
                                node.vec[0],
                                (node.transform[0] + 1)
                            )

            ck = True
        elif node.abs == "obj":
            self.square[node.vec[1]] = self._insert(
                self.square[node.vec[1]],
                node.character,
                specific_=node.vec[0]
            )
            ck = True
        # modificar de ser necesrio
        elif node.abs == "pla":
            ck = True
        else:
            ck = True

        if ck:
            if not exception:
                self.node_list[node.abs].append(node.meta)
                self._set_meta("node_lst", self.node_list)

            self._create_pre_view()

    def del_node(self, node):
        """
        Elimina un objeto/nodo y actualiza "square" 
        """
        if self._check_own(node):
            return

        a = None

        # TODO:CAMBIAR DE SER NECESARIO U AGREGAR
        if node.abs == "stu":
            from nodes.models.structure import Struture

            a = Struture(self, node.vec[0], node.vec[1], node.transform[0], node.transform[1], self.character, False,f"del_stu_{node.id}")
        elif node.abs == "obj":
            from nodes.models.object import Object

            a = Object(self, node.vec[0], node.vec[1], self.character, f"del_obj_{node.id}", False, DATA=None)
        else:
            ...

        n = 0
        for nodes in self.node_list[node.abs]:
            if nodes[0] == node.id:
                self.node_list[node.abs][n - 1] = [a.id, a.name]
            n += 1
        self.add_node(a, True)


if __name__ == "__main__":
    try:
        mapa = Mapa(int(input("¿Cuán ancho quieres que sea?: ")),
                   int(input("¿Cuán largo quieres que sea?: ")),
                   "#",
                   str(input("¿Cual es el nombre del mapa?: ")))
        print(f"X: {mapa.vec[0]}; Y: {mapa.vec[1]}")

        print(f"META DATOS: {mapa.get_meta()}")
        print("MAPA PINTADO: ")
        mapa.get_pre_view()

        print("EL MAPA FUE PINTADO EXITOSAMENTE")
    except:
        print("EL MAPA TUVO UN ERROR AL CREARSE, INTENTE OTRA VEZ")
