from launchpad import *
import threading
from events import *
import os

os.chdir(os.getcwd()+"/cmd")

try:
	lp, mode, lpName = setup_launchpad()
except:
	print("We cannot find a launchpad!")
	exit()
lp.Reset()
print("Connected to launchpad:", lpName)
resetPad(lp, events)
lastBut = (-99,-99)
if lp.Open( 0 ):
	while True:
		if mode == 'Pro' or mode == 'ProMk3':
			buts = lp.ButtonStateXY( mode = 'pro')
		else:
			buts = lp.ButtonStateXY()
		if buts != []:
			if buts[2] > 10:
				for i in events:
					if i["x"] == buts[0] and i["y"] == buts[1]:
						try:
							i["actionDown"](lp, mode)
						except:
							print("There is a problem running this script, or there isn't one defined..")
						resetPad(lp, events)
			if buts[2] == 0 :
				for i in events:
					if i["x"] == buts[0] and i["y"] == buts[1]:
						try:
							i["actionUp"](lp, mode)
						except:
							print("There is a problem running this script, or there isn't one defined..")
						resetPad(lp, events)

