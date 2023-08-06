import os
from EveEN.ENweb import *
WiFi()
from subprocess import DEVNULL, Popen, check_call
import webbrowser
from EveEN.ENlogo import *
from EveEN.ENall import *
from EveEN.ENweather import *
from EveEN.czy import *


def Eve():
    cls()
    starter()
    while True:
        Ebreak()
        Evecommends()

def Evecommends():
    i = 0
    for i in range(25):
        print(" ")
        audio = get_audio()
        if len(czy(audio, HELLO)):
            ENsay(HELLOWORDS)
        if len(czy(audio, TIME)):
            if len(czy(audio, IN)):
                city = audio.lower().split(" " + czy(audio, IN)[0] + " ")[1]
                ENtime(city)
                Evecommends()
            ENlocaltime()
            Evecommends()
        if len(czy(audio, what)):
            if len(czy(audio, IS)):
                if len(czy(audio, YOUR)):
                    if len(czy(audio, NAME)):
                        say("My name is Eve")
                        Evecommends()
        if len(czy(audio, temperature)):
            if len(czy(audio, IN)):
                city = audio.lower().split(" " + czy(audio, IN)[0] + " ")[1]
                ENtemperature(city)
                Evecommends()
        if len(czy(audio, stop)):
            if len(czy(audio, application)):
                ENsay("OK, Goodbye")
                exit()
            if len(czy(audio, listening)):
                ENsay("OK, just say Eve if you want to wake me up")
                Ebreak()
                Evecommends()
        if len(czy(audio, open)):
            if len(czy(audio, DESKTOP)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Desktop")
            if len(czy(audio, DOWNLOADS)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Downloads")
            if len(czy(audio, FAVORITES)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Favorites")
            if len(czy(audio, VIDEOS)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Videos")
            if len(czy(audio, DOCUMENTS)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Documents")
            if len(czy(audio, MUSIC)):
                if len(czy(audio, FOLDER)):
                    os.startfile(f"{user}\\Music")
            if len(czy(audio, web)):
                if len(czy(audio, browser)):
                    ENsay("OK, the browser opens")
                    webbrowser.get('edge').open("google.com")
                    Evecommends()
            if len(czy(audio, youtube)):
                ENsay("OK, the youtube opens")
                webbrowser.get('edge').open("youtube.com")
                Evecommends()
            if len(czy(audio, netflix)):
                ENsay("OK, the netflix opens")
                webbrowser.get('edge').open("netflix.com")
                Evecommends()
            if len(czy(audio, twitch)):
                ENsay("OK, the twitch opens")
                webbrowser.get('edge').open("twitch.com")
                Evecommends()
            if len(czy(audio, TEAMS)):
                ENsay("OK, the teams open")
                webbrowser.get('edge').open("https://teams.microsoft.com/go#")
                Evecommends()
            if len(czy(audio, FACEBOOK)):
                ENsay("OK, the facebook open")
                webbrowser.get('edge').open("facebook.com")
                Evecommends()
            if len(czy(audio, MESSENGER)):
                ENsay("OK, the message open")
                webbrowser.get('edge').open("http://messenger.com/")
                Evecommends()
    ENsay("I'm going to sleep. You can wake me up saying Eve")
    Ebreak()
    Evecommends()







################################################################################\

#if len(czy(audio, )):

################################################################################\ms
DESKTOP = ["desktop"]
DOWNLOADS = ["downloads"]
FAVORITES = ["favorites"]
VIDEOS = ["videos"]
DOCUMENTS = ["documents"]
FOLDER = ['folder']
MUSIC = ["music"]
MESSENGER = ["messenger"]
FACEBOOK = ["facebook"]
TEAMS = ["teams"]
TIME = ["time"]
stop = ["stop"]
what = ["what"]
IS = ["is"]
YOUR = ["your"]
NAME = ["name"]
listening= ["listening"]
open = ["open"]
web = ["web"]
browser = ["browser"]
youtube = ["youtube"]
application = ["application", "app"]
netflix = ["netflix"]
twitch = ["twitch"]
temperature = ["temperature"]
IN = ["in"]
HELLO = ["hello", "hi", "welcome"] #przywitanie
HELLOWORDS = ["Hey, hou are you?"]
################################################################################

user = os.path.expanduser('~')


webbrowser.register('edge',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
