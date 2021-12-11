

def commandFinding(audio, COMMANDS, wake):
    for command in COMMANDS:
        for i in range(len(command)):
            try: 
                if wordFinding(audio, command[i]) and wordFinding(audio, wake):
                    return command[i]
            except:
                print("Pas de commandes trouvés dans ", str(command))


def wordFinding(audio, words):
    if words in audio:
        return True
    else:
        return False
 

def wordSearch(audio, words_list):
    i=0
    while i<len(words_list):
        if audio.count(words_list[i]) > 0:
            return words_list[i]
        else:
            print("Mot ", words_list[i], " introuvable...")
        i+=1

def indexSearch(audio, word):
    for i in range(len(audio.split())):
        if word in audio.split()[i]:
            return i





"""i=0
    while i<len(SEQUENCE_CESI):
        if audio.count(SEQUENCE_CESI[i])>0:
            SEQU_CESI(pathBegin)
        i+=1

def commandFinding(audio, COMMANDS, wake):
    for command in COMMANDS:
        for c in command:
            print(c)
            try:
                if wordFinding(audio, c) and wordFinding(audio, wake):
                    begin=audio.split().index(c)
                    audio_list=audio.split()
                    del audio_list[:begin]
                    return c
            except:
                print("Pas de commandes trouvés dans ", str(command))"""