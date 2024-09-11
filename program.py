import random
import time

#win condition
winCon = 30

#player cash
p = 0
pDead = False

#computer cash
c = 0
cDead = False

pDice = 0
#pDice = random.randint(1,6)
#print(pDice)

cDice = 0
#cDice = random.randint(1,6)
#print(cDice)

#ROUND TEST

#Spelare 
roundtype = 0
# 0 = player
# 1 = Computer
turn = 0

#name = input("What is your name? ")
#print(f"Hello there, {name}!")
def CompareDice(type, t, c, p):
    cEven = True
    if(cDice % 2):
        cEven = True
    else:
        cEven = False


    pEven = True
    if(pDice % 2):
        pEven = True
    else:
        pEven = False

    match = False
    if(t > 1):
        if((cEven and pEven) or (cEven == False and pEven == False)):
            print("We have a match!")
            match = True

    if(type == 0):
        #Computer hurt
        if(match == True):
            p -= cDice
            print(f"Computer ripped out {cDice} lives from Player!")
            print(f"Player now has {p} lives left!")
    else:
        #Player hurt
        if(match == True):
            c -= pDice
            print(f"Player ripped out {pDice} lives from Computer!")
            print(f"Computer now has {c} lives left!")

        


        
        

    
        
    
 

while(pDead == False or cDead == False):    
    turn += 1
    print(f"round: {turn}")
    print(f"player lives: {p}")
    print(f"computer lives: {c}")
    if(roundtype == 1):
        # PLAYER TURN
        roundtype = 0
        print("Player's turn!")
        
        fail = True
        while(fail == True):
            putIn = input("Type [roll] to roll: ")
            if(putIn == "roll"):
                fail = False
                pDice = random.randint(1,6)
                print(f"Player rolled:  {pDice}!")
                p += pDice
                print(f"Player now has: {p} lives!")  
                CompareDice(roundtype, turn, c, p)
            else:
                fail = True
    
     
        
    else:
        # COMPUTER TURN
        
        roundtype = 1
        print("Computer's turn!")
        time.sleep(1) 
        print("Computer is currently pondering...")
        time.sleep(2) 
        cDice = random.randint(1,6)
        print(f"Computer rolled:  {cDice}!")
        c += cDice
        print(f"Computer now has: {c} lives!")
        CompareDice(roundtype, turn, c, p)



        

    print(roundtype)
    





