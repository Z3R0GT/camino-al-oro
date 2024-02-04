#Doc 1.0

from .obj.gen_obj import *
from .wns.gen_wns import *

class Camera(gen_obj, gen_wns):
#####################################################
#       CONSEJO:  coord: list = [-X, X, -Y, Y]      #
#####################################################
    def __init__(self, 
                 MAP,
                 PLA,
                 COORD=[-5, 10, -2, 5],
                 NMO: str= ""):
        N_NUM[4] += 1
        super().__init__(COORD[0], COORD[2], ..., N_ABS[1], N_NUM[4], NMO)
        super().__wns__()
        super().__map__(MAP)
        super().__transform__(COORD[1], COORD[3])

        self.focus = PLA

        self._set_meta("pla", (self.focus.id, self.focus.name))
        self.render_image()
        
    def fp(self):
        """
        Actualiza valor a los fotogramas impresos
        """
        if N_FP[1] < N_FP[0]:
            N_FP[1] += 1
        else:
            N_FP[1] = 0
            
    def render_image(self, is_lock:bool = False):
        """
        Crea una fotograma de la actual vista con base a "vec"(vector) dado en "COORD"  
        """
        self.fp()
        
        self._erase_pre_view()
        self._erase_square()

        #¿ESTA MIRANDO?
        if not is_lock:
            cur_ren_x = self.focus.global_x
            cur_ren_y = self.focus.global_y
        else:
            cur_ren_x = self.focus.vec[0]
            cur_ren_y = self.focus.vec[1]
        
        #CREA EL FOTOGRAMA
        for y in range(self.map.vec[1]):
            if y in range(cur_ren_y + self.vec[1], cur_ren_y + self.transform[1]):
                for x in range(self.map.vec[0]):
                    if x in range(cur_ren_x + self.vec[0], cur_ren_x + self.transform[0]):
                        self.pre_view += self.map.square[y][x]
                if DEFAULT[1]:
                    self.square.append(self.pre_view + f"     line {self.map.abs}: {y}")
                else:
                   self.square.append(self.pre_view)
                self._erase_pre_view()
        self._create_pre_view()




