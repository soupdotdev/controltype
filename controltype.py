import Gamepad as gp
import time
import math
import numpy
import pyautogui as ag

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
    6: "a",
    7: "r",
    8: "s",
    9: "t",
    10: "d",
    11: "h",
    12: "n",
    13: "e",
    14: "i",
    15: "o",
    16: "f",
    17: "p",
    18: "g",
    19: "w",
    20: "j",
    21: "l",
    22: "u",
    23: "y",
    24: "k",
    25: "m",
    26: "b",
    27: "z",
    28: "x",
    29: "c",
    30: "q",
    31: "v",
    32: "7",
    33: "8",
    34: "9",
    35: "0",
    36: "/",
    37: ",",
    38: ".",
    39: "\'",
    40: ";",
    41: "\\",

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
oldcharid = int(0)

keypressed = bool(0)
waspressed = bool(0)

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
        if lslength < lengthminimum:
            lsanglefixed = 6
        rsanglefixed = round(rsangle/60)
        if rsanglefixed == 6:
            rsanglefixed = 0
    
    if rslength > lengthminimum:
        charid = lsanglefixed * 6 + rsanglefixed
        charname = layout[charid]
        keypressed = 1
    else:
        keypressed = 0
        #ag.keyUp(charname)

    if keypressed:
        if not waspressed:
            ag.press(charname)
        waspressed = 1
    else:
        waspressed = 0

    #print(charid)
    print(charname)
    #print(lsangle,rsangle)
    #print(lslength,rslength)
    #print(lsanglefixed,rsanglefixed)
    #print(ls,rs)