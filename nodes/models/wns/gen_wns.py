#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

class gen_wns:
    def __wns__(self):
        self.square = []
        self.pre_view = ""

#####################################################
#                      PRE_VIEW ZONE                #
#####################################################

    def _erase_pre_view(self):
        self.pre_view = ""

    def _create_pre_view(self):
        self._erase_pre_view()

        for line in self.square:
            self.pre_view += f"{line}\n"

    def get_pre_view(self, is_print: bool = False):
        if not is_print:
            print(self.pre_view)
        return self.pre_view

#####################################################
#                      SQUARE ZONE                  #
#####################################################

    def _erase_square(self):
        self.square = []

    def _create_square(self, vec: list):
        for y in range(vec[1]):
            for x in range(vec[0]):
                self.pre_view += self.character
            self.square.append(self.pre_view+f"     line {self.abs}: {y}")
            self._erase_pre_view()
            
#####################################################
#                      FUNC ZONE                    #
#####################################################

    def _create_ln_low_num(self, vec: int):
        n = ""
        m = ""
        l = 0
        for i in range(vec):
            n += f"{(i % 10)}"
            if n[-1] == "0":
                m += f"{l}"
                l += 1
            else:
                m +=" " 

        self.square.append(n)
        self.square.append(m)
        self._erase_pre_view()

    def _create_line(self, coods: list, invert: bool = False):
        for x in range(coods[1]):
            if x == 0 or x == (coods[1]-1):
                if invert:
                    t = f"{self.map.character}" * (coods[0] + 4)
                else:
                    t = f"{self.character}" * coods[0]
            else:
                if invert:
                    t = f"{self.map.character}" + f"{self.character}" * (coods[0] + 2) + f"{self.map.character}"
                else:
                    t = f"{self.character}" + f"{self.map.character}" * (coods[0] - 2) + f"{self.character}"

            self.square.append(t + f"     line {self.abs}:{x}")
            # self.square.append(t)

        self._create_pre_view()


