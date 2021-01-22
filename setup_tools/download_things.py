from io import BytesIO
from zipfile import ZipFile
import urllib.request
import os

print("Downloading NirCMD (for sound control)")
urllib.request.urlretrieve("http://www.nirsoft.net/utils/nircmd-x64.zip", "nircmd.zip")
with ZipFile("nircmd.zip", "r") as zip_ref:
    os.system("mkdir cmd")
    zip_ref.extractall('./cmd/')
os.remove("nircmd.zip") 
print("Done!")

print("Downloading pygame...")
os.system("pip3 install pygame")

print("Downloading launchpad_py...")
os.system("pip3 install gitdir")
os.system("py -m gitdir https://github.com/FMMT666/launchpad.py/tree/master/launchpad_py")

print("Downloading obswebsocket...")
os.system("pip3 install obs-websocket-py")

print("Downloading pynput...")
os.system("pip3 install pynput")

print("Downloading spotify cli...")
os.system("pip3 install spotify-cli")

spotifyAuth = input("Do you want to sign into spotify now? (y/n)")
while spotifyAuth != "y" and spotifyAuth != "n":
    print("Please respond with y or n")
    spotifyAuth = input("Do you want to sign into spotify now? (y/n)")

if spotifyAuth == "y":
    print("Please follow the intructions below:")
    os.system("spotify auth login")
else:
    print("Spotify isn't signed in, run 'spotify auth login' to sign in.")

