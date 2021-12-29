from bs4 import BeautifulSoup
import ListenAndSpeak as las
import Execute as exe
import requests, os

url = 'https://www.tameteo.com/pau/heure-par-heure'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

def getTemperatureToday():
    TemperaturePage = soup.find_all('td', attrs={'class', 'temperatura changeUnitT'})
    TemperatureUnclassified=[]

    for i in range(len(TemperaturePage)):
        TemperatureUnclassified.append(TemperaturePage[i].text)
    
    TemperatureToday=[]

    for j in [0, 1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 23, 24, 25, 27, 28, 29]:
        TemperatureToday.append(TemperatureUnclassified[j])

    TemperatureToday=TemperatureToday[7:]

    return TemperatureToday

def getTemperatureTommorow():
    TemperaturePage = soup.find_all('td', attrs={'class', 'temperatura changeUnitT'})
    TemperatureUnclassified=[]

    for i in range(len(TemperaturePage)):
        TemperatureUnclassified.append(TemperaturePage[i].text)

    TemperatureTommorow=[]

    for k in [32, 33, 35, 36, 37, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61]:
        TemperatureTommorow.append(TemperatureUnclassified[k])

    TemperatureTommorow=TemperatureTommorow[7:]

    return TemperatureTommorow

    
def getTemperatureGap(Day='Today'):
    if Day == 'Today':
        Temperatures=getTemperatureToday()
    if Day == 'Tommorow':
        Temperatures=getTemperatureTommorow()

    maxi=-1000
    mini=1000

    for Temp in Temperatures:
        Temp=int(Temp[:len(Temp)-1])
        if Temp<mini:
            mini=Temp
        if Temp>maxi:
            maxi=Temp

    return mini, maxi


def sayTemperatureToday():

    mini, maxi = getTemperatureGap()

    Text="Aujourd'hui la température ira de " + str(mini) + " degrès à " + str(maxi) + " degrès."
    las.speak(Text)

def sayTemperatureTommorow():

    mini, maxi = getTemperatureGap('Tommorow')

    Text="Demain la température ira de " + str(mini) + " degrès à " + str(maxi) + " degrès."
    las.speak(Text)

