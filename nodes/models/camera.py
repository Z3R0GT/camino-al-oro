from nodes.models.const import const as const

from nodes.models.wns.gen_wns import *
from nodes.models.obj.gen_obj import *
from nodes.models.window import *

class Camera(gen_obj, gen_wns):

    def __init__(self, 
                 MAP,
                 PLA,
                 COORD=[0, 0, 0, 0],
                 NMO: str= ""):
        const.cam += 1
        super().__init__(COORD[0], COORD[2], ..., const.n_abs[1], const.cam, NMO)
        super().__wns__()
        super().__map__(MAP)
        super().__transform__(COORD[1], COORD[3])

        self.focus = PLA

        self._set_meta("pla", (self.focus.id, self.focus.name))
        self.render_image()

    def render_image(self, is_lock:bool = False):

        fp()
        self._erase_pre_view()
        self._erase_square()

        if not is_lock:
            cur_ren_x = self.focus.global_x
            cur_ren_y = self.focus.global_y
        else:
            cur_ren_x = self.focus.vec[0]
            cur_ren_y = self.focus.vec[1]
        
        for y in range(self.map.vec[1]):
            if y in range(cur_ren_y + self.vec[1], cur_ren_y + self.transform[1]):
                for x in range(self.map.vec[0]):
                    if x in range(cur_ren_x + self.vec[0], cur_ren_x + self.transform[0]):
                        self.pre_view += self.map.square[y][x]
                #  TODO: CAMBIO TEST IN Camera BY render_image
                self.square.append(self.pre_view + f"     line {self.map.abs}: {y}")
                # self.square.append(self.pre_view)
                self._erase_pre_view()
        self._create_pre_view()



