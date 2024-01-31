# JUEGO CREADO CON VOP (PRIMERO EN SU CLASE) 
# USANDO LA VERSIÓN 1.0.12.23 DEL MOTOR EN CUESTIÓN
# DISFRUTALO 

from nodes import *

mapa_principal = Map(120, 29, "#", "Mansión")

pared_1 = Struture(mapa_principal, 1, 1, 116, 20, "&", True)

pared_1.edit_geometry([(1, 115, 1), (1, 115, 18)])

#CUADRADO INTERIOR
pared_1.create_geometry("Y", 2, 18, 1, 2)
pared_1.create_geometry("Y", 2, 18, 114, 115)

#CUARTO 1
pared_1.create_geometry("X", 3, 4, 2, 17)
pared_1.create_geometry("X", 9, 10, 2, 17)

pared_1.create_geometry("Y", 2, 10, 16, 17)

#ENTRADA
pared_1.create_geometry("Y", 12, 18, 52, 53)
pared_1.create_geometry("Y", 12, 18, 67, 68)

pared_1.create_geometry("X", 11, 12, 44, 82)
pared_1.create_geometry("Y", 4, 12, 43, 44)
pared_1.create_geometry("Y", 2, 12, 82, 83)

pared_1.create_geometry("X", 4, 5, 44, 82)

#PASADISO 1
pared_1.create_geometry("X", 4, 5, 17, 44)
pared_1.create_geometry("X", 9, 10, 17, 44)

#OTROS
pared_1.create_geometry("Y", 10, 18, 27, 28)

pared_1.create_geometry("X", 8, 9, 83, 115)


door = [(59, 19), (60, 19), (59, 18), (60, 18)]

pared_1.create_door(door, "M")

mapa_principal.add_node(pared_1)

#coord = [(4, )]

player = Player(mapa_principal, 40, 25, "X", ..., "...", ["w", "s", "a", "d"], ...)
mapa_principal.add_node(player)

#cuarto_1 = Struture(mapa_principal, 4, 12,  11, 5, "&", True)
#cuarto_1.set_door([(2, 0), (3, 0), (4, 0), (7, 1), (7, 2), (7, 3)], "M")
#mapa_principal.add_node(cuarto_1)

#mapa_principal.get_pre_view()

start_game(mapa_principal)
input("> ")

