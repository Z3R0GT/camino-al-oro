#Doc V 1.0

from typing_extensions import Literal

from .obj.gen_obj import *
from .wns.gen_wns import *
from .ui.gen_ui import *

class Page(gen_obj, gen_wns, gen_ui):
    
    def __init__(self, 
                 X: int, 
                 Y: int, 
                 CHR: str,
                 NMO: str):
        
        N_NUM[7] += 1
        super().__init__(X, Y, CHR, N_ABS[7], N_NUM[7], NMO)
        super().__wns__()

        if self.id == 0:
            CUR[0] = self
                 
        self._create_line(self.vec)
        self._create_ln_low_num(self.vec[0])
        self._create_pre_view()
    
    def add_btn(self, btn, ):
        

        ...