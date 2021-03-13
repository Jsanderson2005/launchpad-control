# launchpad-control

An app written in python to launch functions when a button is pressed or released.

This uses the [launchpad-py](https://github.com/FMMT666/launchpad.py) library to control the launchpad.

I have currently only tested it on windows, but the main program (without the event modules I have made) should work on Linux or MacOS. I have also only tested it on a Launchpad X. This should theoretically work on other launchpads though.



### To install

Click on 'setup.bat' to install needed libraries to make the program work.



### To run

Click on 'start.bat', it will detect the launchpad and display the buttons.



### To configure Events

Edit `events.py` and import the module you made (this will be a python file saved in `event_modules`) using this statement:

```python
from event_modules import [file name]
```

Then, edit the `events` array to add/change buttons to trigger your functions for example:

```json
{"x": 3, "y": 2, "actionDown": voice.PushTT, "r": 0, "g": 0, "b": 100, "actionUp": voice.PushTToff},
```

The `x` and `y` values are the coordinates of the button that will trigger the function.

The `actionDown` value will trigger the said function set when the button is pressed on the launchpad.

The `actionUp` value will trigger the said function set when the button is released on the launchpad.

The `r`, `g` and `b` values are the LEDs on the buttons. The minimum value of this is `0` and the maximum value is `1`. Please be aware that this might differentiate on different launchpads.



### To configure the mixer

I have included a `mixer.py` module in the `event_modules` folder. This is started when the `volume` button is pressed (on a launchpad X). There are virtual 'faders' for each program on windows. The first one the main system volume, which controls the main volume on windows. Each other controls a certain program set in the `mixer events` variable. You can change which x value each fader is and what program it controls by typing in the program name, for example `Spotify.exe`. When opening the mixer, each fader will be at full, where all lights are lit. At the bottom, the app is muted (hence the red button).



Anything problems, let me know in issues or find me on discord: `Jsanderson#0001`
