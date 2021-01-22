from launchpad import *
import pkgutil
import sys
from event_modules import fun
from event_modules import mixer
from event_modules import obs
from event_modules import spotify
from event_modules import voice
from event_modules import winutils

events = [
	{"x": 8, "y": 8, "actionDown": stop, "r": 100, "g": 0, "b": 0}, 
	{"x": 8, "y": 7, "actionDown": fun.fun, "r": 100, "g": 100, "b": 100},
	{"x": 2, "y": 2, "actionDown": voice.discordMute, "r": 100, "g": 100, "b": 0},  
	{"x": 3, "y": 2, "actionDown": voice.discordDeath, "r": 100, "g": 0, "b": 0},
	{"x": 4, "y": 2, "actionDown": voice.PushTT, "r": 0, "g": 0, "b": 100, "actionUp": voice.PushTToff},
	{"x": 5, "y": 2, "actionDown": voice.PushTM, "r": 50, "g": 0, "b": 100, "actionUp": voice.PushTMoff},
	{"x": 2, "y": 4, "actionDown": obs.scene1, "r": 100, "g": 0, "b": 0},
	{"x": 3, "y": 4, "actionDown": obs.scene2, "r": 0, "g": 100, "b": 0},
	{"x": 4, "y": 4, "actionDown": obs.scene3, "r": 0, "g": 0, "b": 100},
	{"x": 5, "y": 4, "actionDown": obs.scene4, "r": 30, "g": 30, "b": 60},
	{"x": 3, "y": 6, "actionDown": spotify.spotifyPlay, "r": 0, "g": 100, "b": 0},
	{"x": 4, "y": 6, "actionDown": spotify.spotifyPause, "r": 100, "g": 0, "b": 0},
	{"x": 2, "y": 6, "actionDown": spotify.spotifyBack, "r": 100, "g": 100, "b": 100},
	{"x": 5, "y": 6, "actionDown": spotify.spotifyForward, "r": 100, "g": 100, "b": 100},
	{"x": 8, "y": 1, "actionDown": mixer.mixer, "r": 0, "g": 100, "b": 100},
    {"x": 8, "y": 6, "actionDown": winutils.blank, "r": 100, "g": 0, "b": 0},
	{"x": 8, "y": 5, "actionDown": winutils.snippingTool, "r": 100, "g": 100, "b": 0}
]