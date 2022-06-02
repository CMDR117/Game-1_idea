#intro to game and the movement and a puzzle
#X=physical object
#/ = enemy that can attack
#\ = enemy that cant attack
#o = rolly object for puzzle
#= = place where rolly object goes for puzzle
#^ = door
#W = jump upgrade

level_map1 = [
'X                                         XX',
'X                                         ^X',
'X           XX                            ^X',
'X      X         XX     XX                ^X',
'XX                                        ^X',
'X  XX                         o      =X   ^X',
'X        X                  XXXXXXXXXXXXXXXX',
'X    X                                     X',
'XXXXXXXXXXXXXXXXX                          X',
'X   X                 XXXXXX               X',
'X  X                             XXXXXXXXXXX',
'XXX                           XXXXXXXXXXXXXX',
'X P                    XXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_transition1 = [
'                          ',
'                          ',
'                          ',
'                          ',
'                          ',
'P                         ',
'XXXXXXXXXXXXXXXXXXXXXXXXXX']

#intro to combat
level_map2 = [
'                                  ^',
'                                  ^',
'                                  ^',
'                                  ^',
'                                  ^',
'                       o          ^',
'                XX  XXXXXXXXXXX XXX',
'         XXXXX                 \   ',
'      XX                    X  =   ',
'  XX                        XXXXXXX',
'      XX       XXXX                ',
'  XX       \         XX  XX  XX    ',
'      XXXXXXX                   XX ',
'                            XX     ',
'P           \        XXXX          ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map_transition2 = [
'                          ',
'                          ',
'                          ',
'                          ',
'                          ',
'                          ',
'XXXXXXX    XXXXXX    XXXXX']

#all functions in one
level_map3 = [
'                                         ',
'                         X     X         ',   
'   o   X   X    X    o             X     ',
'  XXX               XXX               X  ',
'           /         o        /     =    ',
'    XXXXXXXXXXXXXXXXXXXXXXX XXXXXX XXXXX ',
'XX                         X      X      ',
'   XX   XXX   XX        /                ',
'                     XXXXXX             ^',
'     XX  XX  XX        /        XX      ^',
'  XX               XXXXXXXXX            ^',
'     XXXX      /                        ^',
'            XXXXXXX   XXXX              ^',
'XXXXXXXX                    XXXXXXXXXXXXX']

level_map_transition3 = [
'X                          X',
'X                          X',   
'X       X       X          X',
'X                          X',
'X   X                  XXXXX',   
'X         X                X',
'X      X       X          XX',
'X                  X      XX',
'X                       W XX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']

#boss fight
level_map_final = [
'X                              X',
'X         XX        XX         X',
'X              ZQ              X',
'X    XX  B               XX    X',
'X                              X',
'X XXXX                    XXXX X',
'XL  P                         RX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

#testing world
dev_world = [
'X                                                                                                      ',
'X                                     X                                                                ',
'X                                     X                                                                ',
'X                                     X                                                                ',
'X                                     X                                                                ',
'X                                  XX X                                                                ',
'X                                     X                                                                ',
'X                               XX    X XX                                                             ',
'X                                     X    XX                                                          ',
'X                                  XX X XX                                     XX        XX            ',
'X                    XXXX             X                                  XX                     XX     ',
'X        B                            X                                                                ',
'X                           XX                 XXXXXX  XX  XXXXXX   XXX                             XXX',
'X           X               XX                         XXX  XXXXX                                      ',
'X           X  X  P                   X                XXXX  XXXX                                      ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

tile_size = 30
screen_width = 950 
screen_height = len(level_map_final) * tile_size
print(screen_height)