#cat game
import pygame
from pygame.locals import *
import random 
Coords = [" "," "," "," "," "," "," "," "," "]


def Board(): #Print board
    Board_Var = [
    [Coords[6],"|",Coords[7],"|",Coords[8]],
    ["-----|---------|-----"],
    [Coords[3],"|",Coords[4],"|",Coords[5]],
    ["-----|---------|-----"],
    [Coords[0],"|",Coords[1],"|",Coords[2]]
]
    for x in Board_Var:
        print(x)

def patterns_fun(): #Load Changes to dictionary 
    patterns = {
    "h1": [Coords[0],Coords[1],Coords[2],0,1,2],
    "h2": [Coords[3],Coords[4],Coords[5],3,4,5],
    "h3": [Coords[6],Coords[7],Coords[8],6,7,8],

    "v1": [Coords[0],Coords[3],Coords[6],0,3,6],
    "v2": [Coords[1],Coords[4],Coords[7],1,4,7],
    "v3": [Coords[2],Coords[5],Coords[8],2,5,8],

    "d1": [Coords[0],Coords[4],Coords[8],0,4,8],
    "d2": [Coords[2],Coords[4],Coords[6],2,4,6],
}
    return patterns

def turn(simb): #Input correctly
    d = True
    while d == True:
        pos = input()
        if(pos.isnumeric() == False):           
            print('Please enter valid syntax')
        else:
            if(int(pos) > 10 or int(pos) == 0):
                print('Please enter valid syntax')
            else:
                if(Coords[int(pos)-1] == ' '):
                    Coords[int(pos)-1] = simb
                    d = False
                    return int(pos)-1
                else:
                    print('Box already used, enter new one ')  

def CheckWin(simb): #Check win
    
    patterns = patterns_fun()
    brk = False
    for x in patterns:
        if patterns[x][0] == simb and patterns[x][1] == simb and patterns[x][2] == simb:
            print(simb, ' Won!')
            brk = True
    return brk

def pattern_recognition():    
    patterns = patterns_fun()
    Simbols = ["O","X"]
    for w in Simbols:        
        for x in patterns:
            if patterns[x][0] == patterns[x][1] and patterns[x][0] !=  ' ':
                if patterns[x][1] == w:
                    if Coords[patterns[x][5]] == ' ':
                        Coords[patterns[x][5]] = 'O'
                        outpt = True
                        return outpt
            elif patterns[x][0] == patterns[x][2] and patterns[x][0] !=  ' ':
                if patterns[x][2] == w:
                    if Coords[patterns[x][4]] == ' ':
                        Coords[patterns[x][4]] = 'O'
                        outpt = True
                        return outpt
            elif patterns[x][1] == patterns[x][2] and patterns[x][1] !=  ' ':                 
                if patterns[x][2] == w:  
                    if Coords[patterns[x][3]] == ' ':
                        Coords[patterns[x][3]] = 'O'
                        outpt = True
                        return outpt

def imposPattern_Position(Starter_Position):
    impos_Patterns = {
    "corners": [Coords[0],Coords[2],Coords[6],Coords[8]],
    "middles": [Coords[1],Coords[3],Coords[5],Coords[7]],
    "center": [Coords[4]]
}
    for x in impos_Patterns:
        c = 0
        for y in impos_Patterns[x]:  
            c += 1
            if y == 'X':
                Starter_Position = x
                return Starter_Position, c

def GetCaseCorners(Real_Num,Actual_Position):
    Case1 = {
        "1": [-4,0],
        "2": [-6,+2],
        "3": [-3,+1],
        "4": [-5,-1]
    }
    Case2 = {
        "1": [-8,0],
        "2": [-6,-2],
        "3": [-3,-1],
        "4": [-5,-7]
    }
    match Real_Num:
        case 6:
            for x in Case1:
                for y in Case1[x]:                                        
                    if Actual_Position == Real_Num + int(y):
                        return x
        case 8:
            for x in Case2:

                for y in Case2[x]:
                    if Actual_Position == Real_Num + int(y):
                        return x
        case 2:
            for x in Case1:
                for y in Case1[x]:
                    if Actual_Position == Real_Num - int(y):
                        return x
        case 0:
            for x in Case2:
                for y in Case2[x]:
                    if Actual_Position == Real_Num - int(y):
                        return x

def corners(Pos,Step):
    match Pos:
        case 1: RealNum = 0
        case 2: RealNum = 2
        case 3: RealNum = 6
        case 4: RealNum = 8
    match Step:
        case 1:
            Coords[4] = "O"
        case 2:     
            global CornerCase       
            CornerCase = GetCaseCorners(RealNum,Actual_Position)            
            match int(CornerCase):
                case 1: 
                    if Pos == 2 or 6:
                        Coords[3] = "O"
                    else:
                        Coords[5] = "O"
                case 2: pattern_recognition()
                case 3: pattern_recognition()
                case 4: 
                    match RealNum:
                        case 6: 
                            if Actual_Position == 1: Coords[5] = "O"
                            elif Actual_Position == 5: Coords[1] = "O"
                        case 8: 
                            if Actual_Position == 1: Coords[3] = "O"
                            elif Actual_Position == 3: Coords[1] = "O"
                        case 2: 
                            if Actual_Position == 3: Coords[7] = "O"
                            elif Actual_Position == 7: Coords[3] = "O"
                        case 0: 
                            if Actual_Position == 5: Coords[7] = "O"
                            elif Actual_Position == 7: Coords[5] = "O"
        case 3:
            match int(CornerCase):
                case 1: pattern_recognition()
                case 2: 
                    Output = pattern_recognition()
                    if Output != True:
                        randomNum = random.randrange(1,8,2)
                        while Coords[randomNum] != ' ':
                            randomNum = random.randrange(1,8,2)
                        Coords[randomNum] = "O"
                case _: pattern_recognition()
        case _:
            Output = pattern_recognition()
            if Output != True:
                randomNum = random.randrange(0,8)
                while Coords[randomNum] != ' ':
                    randomNum = random.randrange(0,8)
                Coords[randomNum] = "O"

def Middles(Pos,Step): 
    match Pos:
        case 1: RealNum = 1
        case 2: RealNum = 3
        case 3: RealNum = 5
        case 4: RealNum = 7
    match Step:
        case 1:                        
            if RealNum > 4: Sign = -1             
            else: Sign = 1
            if RealNum == 1 or RealNum == 7:  Reference = 6
            else: Reference = 2                
            print(RealNum + (Reference * Sign))
            Coords[RealNum + (Reference * Sign)] = "O"                
        case 2: 
            global MiddleCase            
            Output = pattern_recognition()
            if Output == True:
                MiddleCase = 1
            else:
                if Actual_Position == 4:
                    MiddleCase = 4
                else:
                    if (Actual_Position % 2) == 0: MiddleCase = 3                        
                    else: MiddleCase = 2
            match MiddleCase:
                case 2:
                    if RealNum == 1 or RealNum == 7: Reference = 1                        
                    else: Reference = 3

                    if Actual_Position > 4: Sign = 1
                    else: Sign = -1

                    Coords[RealNum + (Reference * Sign)] = "O"
                case 3:
                    match RealNum:
                        case 1: 
                            if RealNum + 5  == Actual_Position: Coords[RealNum + 1] = "O"
                            else: Coords[RealNum - 1] = "O"
                        case 3:
                            if RealNum + 5 == Actual_Position: Coords[RealNum - 3] = "O"
                            else: Coords[RealNum + 3] = "O"
                        case 5: 
                            if RealNum - 5 == Actual_Position: Coords[RealNum + 3] = "O"
                            else: Coords[RealNum - 3] = "O"
                        case 7:
                            if RealNum - 5  == Actual_Position: Coords[RealNum - 1] = "O"
                            else: Coords[RealNum + 1] = "O"
                case 4:
                    if RealNum > 4: Coords[0] = "O"
                    else: Coords[8] = "O"
        case 3:
            if MiddleCase == 3:
                Output = pattern_recognition()
                if Output != True:
                    if Actual_Position != 4:
                        Coords[4] = "O"
                    else:
                        randomNum = random.randrange(1,8,2)
                        while Coords[randomNum] != ' ':
                            randomNum = random.randrange(1,8,2)
                        Coords[randomNum] = "O"
            elif MiddleCase == 1:
                Output = pattern_recognition()
                if Output != True:
                    match RealNum:
                        case 1:
                            if Actual_Position == 5 : Coords[6] = "O"
                            else: Coords[3] = "O"
                        case 3: 
                            if Actual_Position == 1 : Coords[8] = "O"
                            else: Coords[2] = "O"
                        case 5:
                            if Actual_Position == 7 : Coords[0] = "O"
                            else: Coords[6] = "O"
                        case 7:
                            if Actual_Position == 3 : Coords[2] = "O"
                            else: Coords[0] = "O"
            else:
                Output = pattern_recognition()
                if Output != True: Coords[4] = "O"
        case _: 
            Output = pattern_recognition()
            if Output != True:
                randomNum = random.randrange(0,8)
                while Coords[randomNum] != ' ':
                    randomNum = random.randrange(0,8)
                Coords[randomNum] = "O"
def Center(Step):
    match Step:
        case 1:
            Coords[2] = "O"
        case 2:
            Output = pattern_recognition()
            if Output != True:
                Coords[8] = "O"
        case _:
            Output = pattern_recognition()
            if Output != True:
                randomNum = random.randrange(0,8)
                while Coords[randomNum] != ' ':
                    randomNum = random.randrange(0,8)
                Coords[randomNum] = "O"
        

                    
def Bot(Step,Actual_Position,Starter_Position):
    if Starter_Position == "":
        Starter_Position = imposPattern_Position(Actual_Position)
    if Starter_Position[0] == "middles":                
        Middles(Starter_Position[1],Step)
    elif Starter_Position[0] == "corners":
        corners(Starter_Position[1],Step)
    elif Starter_Position[0] == "center":
        Center(Step)
    return Starter_Position

Step = 0
Actual_Position = ""
Starter_Position = ""


for y in range(9):  
        if (y % 2) == 0:
            print('X Turn')        
            Actual_Position =  turn('X')
            Board()
            brk = CheckWin('X')
            if(brk):
                break
        else:
            print('O Turn')
            Step += 1            
            Starter_Position = Bot(Step,Actual_Position,Starter_Position)
            Board()
            brk = CheckWin('O')
            if(brk):
                break


