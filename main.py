# JUEGO CREADO CON VOP (PRIMERO EN SU CLASE) 
# USANDO LA VERSIÓN 1.1.12.23 DEL MOTOR EN CUESTIÓN
#V 1.1
# DISFRUTALO 

from nodes import *

DEFAULT[1] = False

mapa_principal = Mapa(120, 29, "#", "Mansión")

mansion = Struture(mapa_principal, 1, 1, 116, 20, "&", True)

mansion.edit_geometry([(1, 115, 1), (1, 115, 18)])

#CUADRADO INTERIOR
mansion.create_geometry("Y", 2, 18, 1, 2)
mansion.create_geometry("Y", 2, 18, 114, 115)

#CUARTO 1
mansion.create_geometry("X", 3, 4, 2, 17)
mansion.create_geometry("X", 9, 10, 2, 17)

mansion.create_geometry("Y", 2, 10, 16, 17)

#ENTRADA
mansion.create_geometry("Y", 12, 18, 52, 53)
mansion.create_geometry("Y", 12, 18, 67, 68)

mansion.create_geometry("X", 11, 12, 44, 82)
mansion.create_geometry("Y", 4, 12, 43, 44)
mansion.create_geometry("Y", 2, 12, 82, 83)

mansion.create_geometry("X", 4, 5, 44, 82)

#PASADISO 1
mansion.create_geometry("X", 4, 5, 17, 44)
mansion.create_geometry("X", 9, 10, 17, 44)

#OTROS
mansion.create_geometry("Y", 10, 18, 27, 28)

mansion.create_geometry("X", 8, 9, 83, 115)

#PUERTA
door = [(59, 19), (60, 19), 
        (59, 18), (60, 18),
        (59,11), (60, 11),
        (59, 4), (60, 4),
        (14, 9), 
        (28, 17), (40, 9),
        (9, 9), 
        (82, 7), (83, 8), (82, 3), 
        (16, 2)]

mansion.create_door(door, "M")

mapa_principal.add_node(mansion)

player = Player(mapa_principal, 40, 25, "X", ..., "...", ["w", "s", "a", "d"], ...)
mapa_principal.add_node(player)

camara_principal = Camera(mapa_principal, player, NMO="a")

CUR[1] = camara_principal
CUR[0] = mapa_principal

start_game(player, False, [20, 14])