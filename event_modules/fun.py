import random
import time

def fun(lp, mode):
	count = 0
	lastBut = (-99,-99)
	tStart = time.time()
	while True:
		if mode == 'Pro' or mode == 'ProMk3':
			buts = lp.ButtonStateXY( mode = 'pro')
		else:
			buts = lp.ButtonStateXY()
		if buts != []:
			if buts[2] > 0:
				lastBut = ( buts[0], buts[1] )
				tStart = time.time()
			else:
				if lastBut == ( buts[0], buts[1] ) and (time.time() - tStart) > 2:
					break
		else:
			x = random.randint(0, 9)
			y = random.randint(0, 9)
			r = random.randint(0, 100)
			g = random.randint(0, 100)
			b = random.randint(0, 100)
			lp.LedCtrlXY( x, y, r, g, b)
	lp.Reset()