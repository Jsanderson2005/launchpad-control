from pynput.keyboard import Key, Controller

def discordMute(lp, mode):
	keyboard = Controller()
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('m')
	keyboard.release('m')
	keyboard.release(Key.shift)
	keyboard.release(Key.ctrl)

def discordDeath(lp, mode):
	keyboard = Controller()
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('d')
	keyboard.release('d')
	keyboard.release(Key.shift)
	keyboard.release(Key.ctrl)

def PushTT(lp, mode):
	keyboard = Controller()
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('p')

def PushTToff(lp, mode):
	keyboard = Controller()
	keyboard.release('p')
	keyboard.release(Key.shift)
	keyboard.release(Key.ctrl)

def PushTM(lp, mode):
	keyboard = Controller()
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('m')
	keyboard.release('m')
	keyboard.release(Key.shift)
	keyboard.release(Key.ctrl)

def PushTMoff(lp, mode):
	keyboard = Controller()
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('m')
	keyboard.release('m')
	keyboard.release(Key.shift)
	keyboard.release(Key.ctrl)