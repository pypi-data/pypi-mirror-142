from bs4 import BeautifulSoup as bs
import requests
import socket
import urllib.request
from EveEN.ENall import *
import time

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def connect():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except OSError:
        return False

def WiFi():
    wifi = connect()
    if wifi==True:
        print("wifi ok")
    if wifi==False:
        print("wifi failed")
        time.sleep("5")
        exit()
#############################wifi###############################################

def gettime(url):

    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)

    soup = bs(html.text, "html.parser")
    result = {}

    result['time'] = soup.find("div", attrs={"role": "heading"}).text
    return result


def ENtime(city):
    url = "https://www.google.com/search?q=time+"
    city2 = city.replace(" ","+")
    url+=city2
    data = gettime(url)
    ENsay("Time is " + data['time'])

def ENlocaltime():
    url = "https://www.google.com/search?q=time"
    data = gettime(url)
    ENsay("Time is " + data['time'])

################################time############################################
