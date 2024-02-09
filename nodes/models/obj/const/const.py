#DOC V 1.0

CUR = [...,    #MAPA     0
       ...]    #CAM      1
"""
Objetos recurrentes mutables, que pueden variar
durante la ejecución del programa
"""

N_ABS = ["obj",  # 0
         "cam",  # 1
         "pla",  # 2
         "npc",  # 3
         "map",  # 4
         "stu",  # 5
         "dlg",  # 6
         "pgn",  # 7
         ]  
"""
abecedario/nombre cortos de los diferentes objetos
"""
N_NUM = [0, #OBJ    0
         0, #PLA    1
         0, #MAPA   2
         0, #NPC    3
         0, #CAM    4
         0, #DLG    5
         0, #STU    6
         0, #PGN    7
         ]
"""
referencia para IDs de los objetos
"""

N_FP = [10,   #LIM_FP             0
        0,    #FP                 1
        0.15  #TIME_PER_FRAME     2
        ]
"""
Referencia de FramesPeer (FP) para configuración de impresión
y consistencia
"""

DEFAULT = ["M",  #DOOR_DEFAULT_CHR    0
           True  #IS_DEV              1
           ]
"""
variables por defecto, NO TOCAR
"""
