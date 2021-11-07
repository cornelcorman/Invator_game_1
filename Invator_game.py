from os import system
from time import sleep
from keyboard import is_pressed

## INPUT DATA
frames = 0

map_width = 10
map_height = 10

invader_x = 3
invader_y = 2

player_x = 2
player_y = 10

while True:
    frames +=1
    system("cls")

    ##   DROW THE MAP ---- RANDER SHOW  ##############
    print()
    for x in range(1, map_width+3):
        print("#", end = " ")
    print()    # "\n"

    for y in range (1, map_height+1):
        print("# ", end="")
        for x in range(1, map_width+1):
            if x == invader_x and y == invader_y:
                print("🤖", end="")
            elif x == player_x and y == player_y:
                print("☺", end=" ")
            else:
                print(".", end = " ")
        print("#")

    for x in range(1, map_width+3):
        print("#", end = " ")
    print()
    print("frames: ", frames)
    print()

    ##   DROW THE MAP ---- RANDER SHOW  ##############
    sleep(0.1)


    ##   INTERACTIV WITH PLAYER ---- RANDER SHOW  ##############
    ##   DECISION MAKING  ---- RANDER SHOW  ##############
    ## HW1 / apply the limits 

    if is_pressed ("a"):
        if player_x > 1:
           player_x -= 1
    if is_pressed ("d"):
        if player_x < 10:
           player_x += 1
    ##   DECISION MAKING  ---- RANDER SHOW  ############## 
    ##   INTERACTIV WITH PLAYER ---- RANDER SHOW  ##############


    
    


    ##   UPDATE DATA  ---- RANDER SHOW  ##############
    ##   UPDATE DATA  ---- RANDER SHOW  ##############

############ 
#..........#
#..........#
#..........#
#..........#
#..........#
#..........#
#..........#

## Special characters


## Diagram / Lifecycle
"""
RANDER SHOW    <------------
  |
  |
  |
INTERACTIVE WITH PLAYER
  |
  |
  |
DECISION MAKING
  |
  |
  |                         
UPDATE DATE  --------------
      



"""
