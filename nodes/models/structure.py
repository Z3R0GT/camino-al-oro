#Doc 1.0
from typing_extensions import Literal

from .wns.gen_wns import *
from .obj.gen_obj import *

class Struture(gen_obj, gen_wns):
    def __init__(self,
                 MAP,
                 X: int,
                 Y: int,
                 SZ_X: int,
                 SZ_Y: int,
                 CHR: str,
                 IS_COLL: bool = False,
                 NMO: str = ""):
        N_NUM[6] += 1
        super().__init__(X, Y, CHR, N_ABS[5], N_NUM[6], NMO)
        super().__map__(MAP)
        super().__wns__()
        super().__transform__(SZ_X, SZ_Y)

        self.is_coll = IS_COLL

        self.__size = []

        if self.is_coll:
            self.map.set_coll(self)

        self._set_meta("is_coll", self.is_coll)

        self._set_meta("size", self.__size)

        self._create_line(self.transform)
        self._create_ln_low_num(self.transform[0])
        self._create_pre_view()

#####################################################
#       CONSEJO:  coord: list =[(X, Y)]             #
#####################################################
    def create_door(self, coods: list = [(0,0)], CHR =""):
        """
        Crea una puerta con base a las coordenadas locales del objeto
        """
        self._erase_pre_view()
        for _in in coods:
            self.square[_in[1]] = self._insert(self.square[_in[1]],
                                                              f"{CHR}",
                                                              specific_=_in[0])
        self._create_pre_view()

    def create_geometry(self, 
                      TYPE:Literal["X", "Y", "-Y"], 
                      LN_Y_FROM:int, 
                      LN_Y_TO:int, 
                      LN_X_FROM:int,
                      LN_X_TO:int,
                      AUTO_APPLY:bool=True):
        """
        Crea y aplica coordenadas más facilmente o retorna la coordenada en cuestión
        """
        coord = []
        
        if TYPE == "Y":
            for line in range(LN_Y_FROM, LN_Y_TO):
                coord.append((LN_X_FROM, LN_X_TO, line))
                
        elif TYPE == "-Y":
            for line in range(LN_Y_TO, LN_Y_FROM, -1):
                coord.append((LN_X_FROM, LN_X_TO, line))
                
        elif TYPE == "X":
            coord.append((LN_X_FROM, LN_X_TO, LN_Y_FROM))
            
        #REGRESA O APLICA LAS VARIABLE
        if AUTO_APPLY:
            self.edit_geometry(coord)
        else:
            return coord



#####################################################
#  CONSEJO:  coord: list =[(FROM, TO, LINE)]        #
#####################################################
    def edit_geometry(self, coord: list = [(0, 0, 0)]):
        """
        Forma basica de crear lineas con coordenadas locales del objeto
        """
        self._erase_pre_view()
        for in_ in range(len(coord)):
            if len(coord[in_]) == 3:
                if type(coord[in_][0] and coord[in_][1] and coord[in_][2]) is type(3):
                    if self.transform[1] <= coord[in_][2]:
                        print(f"la linea ingresada es mayor a la establecida por el objeto \n \
                              INFO: GENERAL: {coord[in_]}")
                        coord[in_] = [coord[in_][0], coord[in_][1], self.transform[1] - 1]
                    self.__size.append(coord[in_])

                    self.square[coord[in_][2]] = self._insert(self.square[coord[in_][2]],
                                                              f"{self.character}" * (coord[in_][1] - coord[in_][0]),
                                                              coord[in_][0],
                                                              coord[in_][1])
                else:
                    print(
                        f"alguno de los datos no es 'int' como se esperaba. \n \
                        INFO: {coord[in_]}")
            else:
                print(
                    f"el N: {in_} comando entragado posee menos de 3 posiciones. \n \
                    INFO: {coord[in_]}")
                
        self.meta["size"].append(coord)
        self._create_pre_view()


if __name__ == "__main__":

    try:
        import time
        from mapa import *

        # SE CREA UN MAPA :D
        mapa = Mapa(50, 30, "#", "k")

        # SE CREA UNA Structure (mi casa :v)
        casa = Struture(mapa, 1, 0, 24, 24, "&")
        casa.get_pre_view()
        print("LA ESTRUCTURA SE CREO CON LOS ATRIBUTOS DADOS, PERO ESTA EN BLANCO")
        time.sleep(5)

        # CREAMOS UN ARRAY (list) PARA LAS COORDENADAS NUEVAS
        coord = [
            (0, 10, 3),
            (0, 10, 10),
        ]
        for i in range(4, 10):
            coord.append((9, 10, i))
        for i in range(20, 23):
            coord.append((11, 12, i))

        # AGREGAMOS LAS PARTES A "casa"
        casa.edit_geometry(coord)
        casa.get_pre_view()
        print("LA ESTRUCTURA ANTES DE SER AGREGADA AL MAPA")
        time.sleep(5)

        # AGREGAMOS AL NODO AL MAPA
        mapa.add_node(casa)
        mapa.get_pre_view()
        print("LA ESTRUCTURA SE AGREGASTE DONDE LO COLOCASTE CON X & Y")
    except:
        print("HUBO UN ERROR AL CREAR LA ESTRUCTURA")
