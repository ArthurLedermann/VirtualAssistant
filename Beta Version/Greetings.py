import ListenAndSpeak as las
import datetime, os, pickle, Meteo

path=r"C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees\lastStart.txt"

def getDateTimeNow():
    yearNow=str(datetime.datetime.now().year)
    monthNow=str(datetime.datetime.now().month)
    dayNow=str(datetime.datetime.now().day)

    hourNow=str(datetime.datetime.now().hour)
    minuteNow=str(datetime.datetime.now().minute)
    secondeNow=str(datetime.datetime.now().second)

    datetimeNow=[[int(yearNow), int(monthNow), int(dayNow)], [int(hourNow), int(minuteNow), int(secondeNow)]]

    return datetimeNow

def getLastConnection():
    with open(path, 'rb') as f:
        myPickler=pickle.Unpickler(f)
        lastDateTime=myPickler.load()
    return lastDateTime


def savelastConnection(dateTimeToSave):
    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(dateTimeToSave)


def greetings():

    lastDateTime=getLastConnection()
    datetimeNow=getDateTimeNow()

    if lastDateTime[0][0]<datetimeNow[0][0]:
        las.speak("Bonjour, je vous souhaite une bonne année !")
    elif (datetimeNow[1][0]<10) and (datetimeNow[1][0]>4) and ((lastDateTime[0][2]<datetimeNow[0][2]) or (lastDateTime[0][1]<datetimeNow[0][1])):
        las.speak("Bonjour, comment allez vous aujourd'hui ?")
        Meteo.sayTemperatureToday()

    else:
        las.speak("Re Bonjour")

    savelastConnection(datetimeNow)
