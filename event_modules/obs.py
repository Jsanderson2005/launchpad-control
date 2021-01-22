from obswebsocket import obsws, requests

def scene1(lp, mode):
	ws = obsws("localhost", 4444, "secret")
	ws.connect()
	ws.call(requests.SetCurrentScene("Streamdeck"))
	ws.disconnect()

def scene2(lp, mode):
	ws = obsws("localhost", 4444, "secret")
	ws.connect()
	ws.call(requests.SetCurrentScene("Display 1"))
	ws.disconnect()

def scene3(lp, mode):
	ws = obsws("localhost", 4444, "secret")
	ws.connect()
	ws.call(requests.SetCurrentScene("Display 2"))
	ws.disconnect()

def scene4(lp, mode):
	ws = obsws("localhost", 4444, "secret")
	ws.connect()
	ws.call(requests.SetCurrentScene("Blank"))
	ws.disconnect()