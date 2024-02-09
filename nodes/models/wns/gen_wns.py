#Doc 1.0

class gen_wns:
    def __wns__(self):
        """
        Objeto que requieren un espacio amplio
        """
        self.square = []
        self.pre_view = ""

#####################################################
#                      PRE_VIEW ZONE                #
#####################################################

    def _erase_pre_view(self):
        """
        Limpia/Borra/Crea la pre-visualización del objeto
        """
        self.pre_view = ""

    def _create_pre_view(self):
        """
        Crea una pre-visualización con base al atributo "square"
        """
        self._erase_pre_view()

        for line in self.square:
            self.pre_view += f"{line}\n"

    def get_pre_view(self, is_print: bool = False):
        """
        Imprime o no la pre-visualización final del objeto
        """
        if not is_print:
            print(self.pre_view)
        return self.pre_view

#####################################################
#                      SQUARE ZONE                  #
#####################################################

    def _erase_square(self):
        """
        Limpia/Borra/Crea el atributo "square" del objeto
        """
        self.square = []

    def _create_square(self, vec: list):
        """
        Crea lina por linea y guarda el "square", usando el "vec" (vector) 
        del objeto
        """
        for y in range(vec[1]):
            for x in range(vec[0]):
                self.pre_view += self.character
            self.square.append(self.pre_view+f"     line {self.abs}: {y}")
            self._erase_pre_view()
            
#####################################################
#                      FUNC ZONE                    #
#####################################################

    def _create_ln_low_num(self, vec: int):
        """
        Crea linea de posición para los diferentes caracteres para
        su ubicación DURANTE el desarrollo
        """
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
        """
        Crea un cubo
        """
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
                    if self.abs == "pgn":
                        t = f"{self.character}" + " " * (coods[0] - 2) + f"{self.character}"
                    else:
                        t = f"{self.character}" + f"{self.map.character}" * (coods[0] - 2) + f"{self.character}"

            self.square.append(t + f"     line {self.abs}:{x}")
            # self.square.append(t)

        self._create_pre_view()

    def _edit_line(self, coods: list = [(0,0)], CHR =""):
        """
        Edita una linea base a las coordenadas propocionadas, insertar la cadena de caracteres de "CHR"
        """
        self._erase_pre_view()
        len_chr = len(CHR)
        
        if self.abs == "pgn":
            d = True
        else:
            d = False
        
        for _in in coods:
            if not d:
                self.square[_in[1]] = self._insert(self.square[_in[1]], f"{CHR}", specific_=_in[0])
            else:
                if len_chr >= self.vec[0]:
                    self.square[_in[1]] = self._insert(self.square[_in[1]], f"{CHR}", from_=_in[0], to_=self.vec[0])
                    self.square[_in[1]] = self._insert(self.square[_in[1]], f"{self.character}", specific_=self.vec[0]-1)
                    return True, int(len_chr-self.vec[0])
                else:
                    self.square[_in[1]] = self._insert(self.square[_in[1]], f"{CHR}", from_=_in[0], to_=_in[0]+len_chr)
                    return False, 0
                    
            
        self._create_pre_view()

