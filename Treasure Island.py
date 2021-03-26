print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('''
Welcome to Treasure Island.
---------------------------

After a hard sail to the isle of Skulls you disembark
only to find you way blocked by a vertical wall of vegetation
covering an impossible to climb cliff. There are only two
choices, left or right.
''')

print("What do you choose, left or right?")
print("                    ----    -----\n\n")

# Game over variable and choice text
go = 0 

# Get user input and turn it to lower case
direction = input().lower()

if direction == "left":
    go = 0
else:
    go = 1
    
if go == 0:
    print('''
You turn left and make your way down an overgrown path towards
empty darkness. Wait! You see something glitter at the end, could 
it be the treasure or another trap. But between you and the 
glittering prizes you realise is a river you need to cross.
          
Do you swim or abandon you quest?
       ----    -------
                 
          ''')
    swim = input().lower()
    if swim  == "abandon":
        go = 0
    else:
        go = 1
        
if go == 0:
    print('''
You abandon the quest, and sit on a rock to think about your 
next move. Suddenly the rock sinks into the sand and with an 
earth shattering sound a cave opens up in the cliff
revealing Captain Easy Clap's treasure.
          
          ''')
else:
    go = 1
    
if go == 1:
    print('''
          You big fat loser. 
          You die.
          
          ''')
else:
    print('''success is yours but you awaken from your dream.
          Back to work sucker.
          ''')
    
print("T H E   E N D")
    