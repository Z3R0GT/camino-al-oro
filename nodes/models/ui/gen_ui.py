
from typing import Literal


class gen_ui():

    def create_text(self, text: str, line: Literal["CENTER", "UPPER", "LOWER", "CUSTOM"], LINE:list=("X","Y"), chk=True):   
        """
        Crea/Inserta texto en la pagina, puedes usar las prefabricadas o "CUSTOM"izar la linea, para ello, tendras que usar "LINE"
        """
        global ver            

        def __check():
            if ver[0]:
                __recursive()
        
        def __recursive():
            temp = []
            new = ""
            for i in range(len(text)-ver[1], len(text)):
                temp.append(text[i])
                
            for i in range(len(temp)):
                new += temp[i]
            
            self.create_text(new, line, (LINE[0], LINE[1]+1), False)
            
        self._erase_pre_view()
        if line == "CUSTOM":
            
            ver = self._edit_line([LINE], text)
            __check()
        elif line == "UPPER":
            
            if chk:
                LINE = (1,1)
            ver = self._edit_line([LINE], text)
            __check()
        elif line == "CENTER":
            
            if chk:
                LINE = (int(self.vec[0]/2)-5, int(self.vec[1]/2))
            
            ver = self._edit_line([LINE], text)
            __check()
        elif line == "LOWER":
            
            if chk:
                LINE = (1, self.vec[1]-2)
            ver = self._edit_line([LINE], text)
            print("ME DA PEREZA COLOCAR PARA QUE AGREGUE UNA NUEVA LINEA AUTOMATICAMENTE SI?, COMPRENDE")

        self._create_pre_view()
        
    