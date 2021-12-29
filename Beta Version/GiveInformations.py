import nextSpaceFlight as Nsp
import Meteo

def whatToSay(audio):

    if ('fusée' in audio) and (('dis' in audio) or ('donne' in audio)):
        Nsp.getNextFlights()
    elif ('fusée' in audio) and ('affiche' in audio):
        Nsp.getNextFlightsDisplay()
    elif 'météo' in audio:
        if 'demain' in audio:
            Meteo.sayTemperatureTommorow()
        else:
            Meteo.sayTemperatureToday()