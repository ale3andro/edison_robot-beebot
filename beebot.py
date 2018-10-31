#-------------Setup----------------

import Ed
Ed.PlayMyBeep(8000)
Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------
moves = Ed.List(15)
for x in range(15):
    moves[x]=-1
moves_index = 0
start = 0

Ed.PlayBeep()
Ed.ReadKeypad()
#Ed.ReadRemote()
Ed.LeftLed(Ed.ON)
Ed.RightLed(Ed.ON)

while start==0: 
    pressed_button = Ed.ReadKeypad()
    ir_code = Ed.ReadRemote()
    
    # Ed.REMOTE_CODE_0 --> Up Arrow
    # Ed.REMOTE_CODE_1 --> Down Arrow
    # Ed.REMOTE_CODE_2 --> Left Arrow
    # Ed.REMOTE_CODE_3 --> Right Arrow
    
    if (moves_index<14):
        if (ir_code==Ed.REMOTE_CODE_0):
            moves[moves_index]=0
            moves_index+=1
            Ed.PlayBeep()
        if (ir_code==Ed.REMOTE_CODE_1):
            moves[moves_index]=1
            moves_index+=1
            Ed.PlayBeep()
        if (ir_code==Ed.REMOTE_CODE_2):
            moves[moves_index]=2
            moves_index+=1
            Ed.PlayBeep()
        if (ir_code==Ed.REMOTE_CODE_3):
            moves[moves_index]=3
            moves_index+=1
            Ed.PlayBeep()
    else:
        Ed.PlayMyBeep(8000)
            
    if (pressed_button==Ed.KEYPAD_TRIANGLE):
        start=1 
        Ed.PlayMyBeep(8000)
        

for y in range(2):
    Ed.PlayBeep()
    Ed.TimeWait(1, Ed.TIME_SECONDS)
    
Ed.LeftLed(Ed.OFF)
Ed.RightLed(Ed.OFF)

for x in range(15):
    if moves[x]==0:
        Ed.Drive(Ed.FORWARD, Ed.SPEED_2, 10)
    elif moves[x]==1:
        Ed.Drive(Ed.BACKWARD, Ed.SPEED_2, 10)
    elif moves[x]==2:
        Ed.Drive(Ed.SPIN_LEFT, 10, 90)
    elif moves[x]==3:
        Ed.Drive(Ed.SPIN_RIGHT, 10, 90)
        
            