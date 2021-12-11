import os
from search import indexSearch


recherche=["recherche", "recherches", "rechercher", "regarde", "regarder"]

def research(audio, c):
    print(audio)
    print(c)
    begin=indexSearch(audio, c)
    audio_list=audio.split()
    del audio_list[:begin+1]
    print(audio_list)
    searchBegin="https://www.ecosia.org/search?q="
    searchEnd="&addon=firefox&addonversion=4.0.4"
    searchMiddle=""
    for i in range(len(audio_list)):
        searchMiddle=searchMiddle + "{}+".format(audio_list[i])
    search=searchBegin + searchMiddle + searchEnd
    
    os.startfile(search)
