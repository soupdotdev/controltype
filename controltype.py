import Gamepad as gp
import time
import math
import numpy

# meow mrrp :3

gamepadType = gp.Xbox360

gamepad = gamepadType()

lengthminimum = 0.99

# THIS IS WHERE THE LAYOUT GOES!!! in the future this may be moved to an xml or something like that but who knows <3
layout = {

    0: "1",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "A",
    7: "R",
    8: "S",
    9: "T",
    10: "D",
    11: "H",
    12: "N",
    13: "E",
    14: "I",
    15: "O",
    16: "F",
    17: "P",
    18: "G",
    19: "W",
    20: "J",
    21: "L",
    22: "U",
    23: "Y",
    24: "K",
    25: "M",
    26: "B",
    27: "Z",
    28: "X",
    29: "C",
    30: "Q",
    31: "V",
    32: "7",
    33: "8",
    34: "9",
    35: "0",

}

ls = [0.0,0.0] #left stick
rs = [0.0,0.0] #right stick
lsangle = 0.0
rsangle = 0.0
lslength = 0.0
rslength = 0.0
lsanglefixed = 0.0
rsanglefixed = 0.0

charid = int(0)
charname = str("")

while gamepad.isConnected():

    eventType, control, value = gamepad.getNextEvent()
    
   # if eventType == "BUTTON":
        #print(str(eventType)+', '+str(control)+', '+str(value))
    
    if eventType == "AXIS":
        if control == "RIGHT-X":
            rs[0] = value
            if abs(rs[0]) < 0.2:
                rs[0] = 0
        if control == "RIGHT-Y":
            rs[1] = value
            if abs(rs[1]) < 0.2:
                rs[1] = 0
        if control == "LEFT-X":
            ls[0] = value
            if abs(ls[0]) < 0.2:
                ls[0] = 0
        if control == "LEFT-Y":
            ls[1] = value
            if abs(ls[1]) < 0.2:
                ls[1] = 0
        
        lsangle = math.degrees(numpy.arctan2(ls[1],ls[0])) + 180
        rsangle = math.degrees(numpy.arctan2(rs[1],rs[0])) + 180
        lslength = math.hypot(ls[0],ls[1])
        rslength = math.hypot(rs[0],rs[1])

        
        lsanglefixed = round(lsangle/60)
        if lsanglefixed == 6:
            lsanglefixed = 0
        rsanglefixed = round(rsangle/60)
        if rsanglefixed == 6:
            rsanglefixed = 0
    
    if lslength > lengthminimum and rslength > lengthminimum:
        charid = lsanglefixed * 6 + rsanglefixed
        charname = layout[charid]

    #print(charid)
    print(charname)
    #print(lsangle,rsangle)
    #print(lslength,rslength)
    #print(lsanglefixed,rsanglefixed)
    #print(ls,rs)