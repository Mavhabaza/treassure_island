print('''
8b,dPPYba,  8b,dPPYba, ,adPPYYba, 8b       d8  ,adPPYba, 8b,dPPYba,  
88P'    "8a 88P'   "Y8 ""     `Y8 `8b     d8' a8P_____88 88P'   "Y8  
88       d8 88         ,adPPPPP88  `8b   d8'  8PP""""""" 88          
88b,   ,a8" 88         88,    ,88   `8b,d8'   "8b,   ,aa 88          
88`YbbdP"'  88         `"8bbdP"Y8     Y88'     `"Ybbd8"' 88          
88                                    d8'                            
88                                   d8'                             

''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure, good luck!.")

answer = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'.\n")
if answer.lower() == "left":
    answer = input("You have come to the Lake. would you like to swim or wait?\n Type 'wait' to wait or 'swim' to swim.\n")
    if answer.lower() == "wait":
        answer = input("You're on an Island and mistry doors apeared before you. which door color would you like to enter?\n Choose 'Red', 'Yellow' or 'Blue'.\n")
        if answer.lower() == "yellow":
            answer = input("The room only has one treasure and it's not enough to sustain your life, what would you do?\n Type 'Leave' to leave the room or 'Search' to search for more treasures.\n")
            if answer.lower() == "search":
                print("You got bitten by a hidden Black Mamba snake and died, Game Over.")
            elif answer.lower() == "leave":
                print("There is swarm of bees on your way out and they attacked and killed you, Game Over.")

            else:
                print("Invalid input, try again next time. Game Over")
        elif answer.lower() == "red":
            print("Burned by fire. Game Over.")
        elif answer.lower() == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over.")

    else:
        print("You have been attacked by trout. Game Over")

elif answer.lower() == "right":
    option = input("You made the right choice, would you like to Drive or to Run?.\n Type 'drive' to drive or 'run' to run.\n")
    if option.lower() == "drive":
        option1 = input("You still have half tank of fuel, and filling station is half a mile ahead, would you like to stop or to pass?.\n Type 'pass' to pass or 'stop' to refill your fuel.\n")
        if option1.lower() == "stop":
            option2 = input("While are still filling it began to rain heavily, do you want to continue witht the journey or to wait?.\n Type 'wait' to wait or 'continue' to continue.\n")
            if option2.lower() == "continue":
                print("While driving you came to a flooded area and you drowned and died. Game Over!.")

            else:
                print("You made the correct choice, the Treasure was hidden on the filling station. You Win!")
                print("""
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                              ,@'
                        :8K  j8
                         "*w*"

Mavhabaza
                """)
        else:
            print("Another station is about 1230 miles away, you ran out of fuel. Game Over.")
    else:
        print("You ran into a group of ganstas and they killed you. Game Over.")
else:
    print("Invalid option, try again next time!. Game Over.")
 