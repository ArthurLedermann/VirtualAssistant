import os, pickle
import CommandsGestionner as Cg

def findCommandLabel(audio):
    allCommands=Cg.getCommands()
    allCommandsKeys=list(allCommands.keys())
    for key in allCommandsKeys:
        for command in allCommands[key]:
            if command in audio:
                return key

def findCommand(audio):
    allCommands=Cg.getCommands()
    allCommandsKeys=list(allCommands.keys())
    for key in allCommandsKeys:
        for command in allCommands[key]:
            if command in audio:
                return command