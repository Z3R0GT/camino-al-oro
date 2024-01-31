# JUEGO CREADO CON VOP (PRIMERO EN SU CLASE) 
# USANDO LA VERSIÓN 1.0.12.23 DEL MOTOR EN CUESTIÓN
# DISFRUTALO 

from nodes import *

mapa_principal = Map(120, 29, "#", "Mansión")

pared_1 = Struture(mapa_principal, 1, 1, 116, 20, "&", True)
coord = [(1, 115, 1),
         (1, 115, 18)]

for right_y in range(2, 18):
    coord.append((1, 2, right_y))
    coord.append((114, 115, right_y))

pared_1.edit_geometry(coord)
door = [(59, 19), (60, 19), (59, 18), (60, 18)]

pared_1.set_door(door, "M")

mapa_principal.add_node(pared_1)

pared_1.get_pre_view()
#coord = [(4, )]

player = Player(mapa_principal, 40, 25, "X", ..., "...", ["w", "s", "a", "d"], ...)
mapa_principal.add_node(player)

#cuarto_1 = Struture(mapa_principal, 4, 12,  11, 5, "&", True)
#cuarto_1.set_door([(2, 0), (3, 0), (4, 0), (7, 1), (7, 2), (7, 3)], "M")
#mapa_principal.add_node(cuarto_1)

#mapa_principal.get_pre_view()
start_game(mapa_principal)
input("> ")

