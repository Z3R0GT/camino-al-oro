from nodes.models.const import const as const

import time as tm
_lim_fp = 10
_fp = 0
time_per_frame = 0.15

def set_lim_fp(lim: int):
    """
    Presenta un limite a los fotogramas (fp)

    :param lim: limite
    :return:
    """
    global _lim_fp
    _lim_fp = lim


def fp():
    """
    da valor a los fotogramas impresos
    :return:
    """
    global _fp, _lim_fp
    if _fp < _lim_fp:
        _fp += 1
    else:
        _fp = 0

def _erase_wns():
    """
    limpia la consola sea el SO utilizado
    :return:
    """
    import os

    os.system("cls")

class Window:
    def __init__(self, 
                 PLA, 
                 MAP, 
                 CAM, 
                 NMO: str = "") -> None:
        const.wns += 1

        self.abs = const.n_abs[7]
        self.id = const.wns

        self.pla = PLA

        self.map = MAP

        self.cam = CAM

        self.name = NMO
    
    def set_map_n_start(self):

        self.pla.move()

        while not self.map.end:
            if not self.map.pause:
                self.cam.render_image()

                _erase_wns()

                self.cam.get_pre_view()
                tm.sleep(time_per_frame)
            
            if self.map.end:
                break
    
    def quite_n_end(self):
        self.map.end = True