from bs4 import BeautifulSoup
import ListenAndSpeak as las
import Execute as exe
import requests, os

url = 'https://nextspaceflight.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')


def getNextFlightsBuisness():
    nextFlightsBuisnessPage = soup.find_all('div', attrs={'class', 'mdl-card__title-text'})
    nextFlightsBuisness=[]

    for i in [0, 2, 4]:
        nextFlightsBuisness.append(nextFlightsBuisnessPage[i].text[32:len(nextFlightsBuisnessPage[i].text)-28])

    return nextFlightsBuisness

def getNextFlightsRocketsNames():
    nextFlightsRocketsNamePage = soup.find_all('h5', attrs={'class', 'header-style'})
    nextFlightsRocketsName=[]
 
    end=24

    for i in range(3):
        for j in range(len(nextFlightsRocketsNamePage[i].text)):
            if nextFlightsRocketsNamePage[i].text[j]=='|':
                end=j

        nextFlightsRocketsName.append(nextFlightsRocketsNamePage[i].text[21:end])

    return nextFlightsRocketsName

def getNextFlightsDate():
    nextFlightsDatePage = soup.find_all('div', attrs={'class', 'mdl-card__supporting-text'})
    nextFlightsDate=[]

    for i in range(3):
        for j in range(len(str(nextFlightsDatePage[i])[39:len(str(nextFlightsDatePage[i]))-6])):

            if str(nextFlightsDatePage[i])[34:len(str(nextFlightsDatePage[i]))-6][j]=='<':
                end=j
                nextFlightsDate.append(str(nextFlightsDatePage[i])[93:end-16])

    return nextFlightsDate
    

def getNextFlights():

    las.speak('Les prochains lancements sont')

    for i in range(3):
        if i==3:
            las.speak(' et ')
        nextFlights="Le ou la " + str(getNextFlightsRocketsNames()[i]) + ' de ' + str(getNextFlightsBuisness()[i])
        las.speak(nextFlights)

def getNextFlightsDisplay():
    exe.execute('nextspaceflights')
