import os
import time

global mixerEvents
mixerEvents = [{"x": 1, "app": "Spotify.exe", "volume": 1}, {"x": 2, "app": "Discord.exe", "volume": 1}, {"x": 3, "app": "Teams.exe", "volume": 1}, {"x": 4, "app": "Firefox.exe", "volume": 1}]
global mainVolume
mainVolume = {"volume": 1}

def setSystemVolume(volume, appName):
	os.system('nirCmd.exe setappvolume {} {}'.format(appName, volume))

def mixer(lp, mode):
    lp.Reset()
    count = 0
    lastBut = (-99,-99)
    lp.LedCtrlXY( 8, 1, 100, 100, 100)
    for y in range(mainVolume['volume']):
        lp.LedCtrlXY( 0, y, 0, 0, 0)
    for y in range(mainVolume['volume'], 8):
        lp.LedCtrlXY( 0, y, 100, 100, 100)
    lp.LedCtrlXY( 0, 8, 100, 0, 0)
    for i in mixerEvents:
        for y in range(i["volume"]):
            lp.LedCtrlXY( i["x"], y, 0, 0, 0)
        for y in range(i["volume"], 8):
            lp.LedCtrlXY( i["x"], y, 100, 100, 100)
        lp.LedCtrlXY( i["x"], 8, 100, 0, 0)
    while True:
        if mode == 'Pro' or mode == 'ProMk3':
            buts = lp.ButtonStateXY(mode = 'pro')
        else:
            buts = lp.ButtonStateXY()
        if buts != []:
            if buts[2] > 0:
                count = 0
                for i in mixerEvents:
                    if buts[0] == 0:
                        volume = 65535 - (buts[1]*8191.875)
                        for y in range(buts[1]):
                            lp.LedCtrlXY( buts[0], y, 0, 0, 0)
                        for y in range(buts[1], 8):
                            lp.LedCtrlXY( buts[0], y, 100, 100, 100)
                        os.system("nirCmd.exe setsysvolume " + str(volume))
                        mainVolume['volume'] = buts[1]
                    elif i["x"] == buts[0] and buts[1] != 0:
                        volume = (100 - (buts[1]*10) - 20)/100
                        for y in range(buts[1]):
                            lp.LedCtrlXY( buts[0], y, 0, 0, 0)
                        for y in range(buts[1], 8):
                            lp.LedCtrlXY( buts[0], y, 100, 100, 100)
                        setSystemVolume(volume ,i["app"])
                        mixerEvents[count]["volume"] = buts[1]
                    if buts[0] == 8 and buts[1] == 1:
                        lp.Reset()
                        return
                    count += 1
    lp.Reset()