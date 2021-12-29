import os
import CommandChecker as Cc

def keepInterest(audio):
    command = Cc.findCommand(audio)
    audio_list=audio.split()

    for i in range(len(audio_list)):
        if command in audio_list[i]:
            del audio_list[:i+1]

    return ' '.join(audio_list)

def research(audio):
    path = "https://www.ecosia.org/search?q=" + keepInterest(audio) + "&addon=firefox&addonversion=4.0.4"
    os.startfile(path)
