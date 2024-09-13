import random
import time

#win condition
winCon = 20

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

pauseTime = 0.8

#name = input("What is your name? ")
#print(f"Hello there, {name}!")

def Message(msg, mult):
    print(msg)
    time.sleep(pauseTime+mult) 

    

def CompareDice(type, t, lives):
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
            Message("BUT... we have a match!", 1)
            match = True

    if(type == 0):
        if(lives >= winCon):
            Message("Player Won!", 0)
            exit(1)
        if(lives <= 0):
            Message("Computer Won!", 0)
            exit(1)
        #Computer hurt
        if(match == True):
            lives = p
            lives -= cDice
            Message(f"Computer ripped out {cDice} lives from Player!", 0)
            #Message(f"Player now has {p} lives left!", 0)
        
            
    else:
        if(lives >= winCon):
            Message("Computer Won!", 0)
            exit(1)
        if(lives <= 0):
            Message("Player Won!", 0)
            exit(1)
        #Player hurt
        if(match == True):
            lives = c
            lives -= pDice
            Message(f"Player ripped out {pDice} lives from Computer!", 0)
            #Message(f"Computer now has {c} lives left!", 0)
        

            

    #RETURN C,P!!!!!!!!!!!

    


    return lives


        
        

    
        
    
 

while(pDead == False or cDead == False):    
    turn += 1
    Message(f"round: {turn}", 0)
    Message(f"player's lives: {p}", 0)
    Message(f"computer's lives: {c}", 0)
    time.sleep(pauseTime) 
    if(roundtype == 1):
        # PLAYER TURN
        roundtype = 0
        Message("Player's turn!", 0)
        
        fail = True
        while(fail == True):
            putIn = input("Type [roll] to roll: ")
            if(putIn == "roll"):
                fail = False
                pDice = random.randint(1,6)
                Message(f"Player rolled:  {pDice}!", 0)
                p += pDice
                Message(f"Player now has: {p} lives!", 0)
                p = CompareDice(roundtype, turn, p)
            else:
                fail = True
    
     
        
    else:
        # COMPUTER TURN
        
        roundtype = 1
        Message("Computer's turn!", 0)
        print("Computer is currently pondering...")
        time.sleep(2) 
        cDice = random.randint(1,6)
        Message(f"Computer rolled:  {cDice}!", 0)
        
        c += cDice
        Message(f"Computer now has: {c} lives!", 0)
        
        c = CompareDice(roundtype, turn, c)



        

    #print(roundtype)
    





