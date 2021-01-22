import os

def snippingTool(lp, mode):
	os.popen('snippingtool')

def blank(lp, mode):
	os.popen('nirCmd.exe monitor off')
	count = 0
	lastBut = (-99,-99)
	tStart = time.time()
	while True:
		if mode == 'Pro' or mode == 'ProMk3':
			buts = lp.ButtonStateXY(mode = 'pro')
		else:
			buts = lp.ButtonStateXY()
		if buts != []:
			if buts[2] > 0:
				lastBut = ( buts[0], buts[1] )
				tStart = time.time()
			else:
				if lastBut == ( buts[0], buts[1] ) and (time.time() - tStart) > 2:
					os.popen('nirCmd.exe monitor on')
					return
		else:
			lp.Reset()