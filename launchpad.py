import launchpad_py as launchpad

MK2_NAME = "Launchpad MK2"
# MK3MINI_NAME = "LPMiniMK3"
MK3MINI_NAME = "minimk3"
PRO_NAME = "Launchpad Pro"
LPX_NAME = "lpx"
CTRL_XL_NAME = "control xl"
LAUNCHKEY_NAME = "launchkey"
DICER_NAME = "dicer"

PAD_MODES = {
    launchpad.Launchpad: "Mk1",
    launchpad.LaunchpadMk2: "Mk2",
    launchpad.LaunchpadMiniMk3: "Mk3",
    launchpad.LaunchpadPro: "Pro",
    launchpad.LaunchpadLPX: "Mk3"
}
PAD_TEXT = {
    launchpad.Launchpad: "Classic/Mini/S",
    launchpad.LaunchpadMk2: "MkII",
    launchpad.LaunchpadMiniMk3: "Mk3",
    launchpad.LaunchpadPro: "Pro (BETA)",
    launchpad.LaunchpadLPX: "LPX"
}

def stop(lp, mode):
	lp.Reset()
	lp.Close()
	exit()

def resetPad(lp, eventsList):
	lp.LedCtrlXY( 8, 0, 255, 255, 255)
	for i in eventsList:
		r = i["r"]
		g = i["g"]
		b = i["b"]
		x = i["x"]
		y = i["y"]
		lp.LedCtrlXY( x, y, r, g, b)

def get_launchpad():
    lp = launchpad.Launchpad()

    if lp.Check(0, MK2_NAME):
        return launchpad.LaunchpadMk2()
    # the MK3 has two midi devices, we need the second one
    if lp.Check(1, MK3MINI_NAME):
        return launchpad.LaunchpadMiniMk3()
    if lp.Check(0, PRO_NAME):
        return launchpad.LaunchpadPro()
    if lp.Check(1, LPX_NAME):
        return launchpad.LaunchpadLPX()

    # unsupported pads
    if lp.Check(0, CTRL_XL_NAME) or lp.Check(0, LAUNCHKEY_NAME) or lp.Check(0, DICER_NAME):
        return -1

    if lp.Check():
        return lp

    return None

def setup_launchpad():
    mode = None

    if launchpad.LaunchpadPro().Check( 0 ):
        lp = launchpad.LaunchpadPro()
        if lp.Open( 0 ):
            lpName = "Launchpad Pro"
            mode = "Pro"

    elif launchpad.LaunchpadProMk3().Check( 0 ):
        lp = launchpad.LaunchpadProMk3()
        if lp.Open( 0 ):
            lpName = "Launchpad Pro Mk3"
            mode = "ProMk3"

    elif launchpad.LaunchpadMiniMk3().Check( 1 ):
        lp = launchpad.LaunchpadMiniMk3()
        if lp.Open( 1 ):
            lpName = "Launchpad Mini Mk3"
            mode = "MiniMk3"

    elif launchpad.LaunchpadLPX().Check( 1 ):
        lp = launchpad.LaunchpadLPX()
        if lp.Open( 1 ):
            lpName = "Launchpad X"
            mode = "LPX"
			
    elif launchpad.LaunchpadMk2().Check( 0 ):
        lp = launchpad.LaunchpadMk2()
        if lp.Open( 0 ):
            lpName = "Launchpad Mk2"
            mode = "Mk2"

    elif launchpad.Dicer().Check( 0 ):
        lp = launchpad.Dicer()
        if lp.Open( 0 ):
            lpName = "Dicer"
            mode = "Dcr"

    elif launchpad.MidiFighter64().Check( 0 ):
        lp = launchpad.MidiFighter64()
        if lp.Open( 0 ):
            lpName = "Midi Fighter 64"
            mode = "F64"

    elif launchpad.Launchpad().Check( 0 ):
        lp = launchpad.Launchpad()
        if lp.Open( 0 ):
            lpName = "Launchpad Mk1/S/Mini"
            mode = "Mk1"

    if mode == None:
        return None

    return lp, mode, lpName

"""
def get_display_name(pad):
    cls = type(pad)

    if cls not in PAD_TEXT:
        return "Unsupported"

    return PAD_TEXT[cls]

def get_mode(pad):
    cls = type(pad)

    if cls not in PAD_MODES:
        return None

    return PAD_MODES[cls]


def pad():
    cls = type(pad)

    if cls not in PAD_TEXT:
        return "Unsupported"

    return PAD_TEXT[cls]


def connect(pad):
    mode = get_mode(pad)

    if mode == "Mk3":
        return pad.Open(1)

    return pad.Open()


def disconnect(pad):
    pad.Close()
"""