import json
import re

notesString = input("Input json string: ")

data = json.loads(notesString)

notesList = []
timeList = []

for currentNote in data["songNotes"]:
    keyInput = currentNote["key"]
    inputKey10 = keyInput.replace("1Key10", "Z")
    inputKey11 = inputKey10.replace("1Key11", "X")
    inputKey12 = inputKey11.replace("1Key12", "C")
    inputKey13 = inputKey12.replace("1Key13", "V")
    inputKey14 = inputKey13.replace("1Key14", "B")
    inputKey0 = inputKey14.replace("1Key0", "Q")
    inputKey1 = inputKey0.replace("1Key1", "W")
    inputKey2 = inputKey1.replace("1Key2", "E")
    inputKey3 = inputKey2.replace("1Key3", "R")
    inputKey4 = inputKey3.replace("1Key4", "T")
    inputKey5 = inputKey4.replace("1Key5", "A")
    inputKey6 = inputKey5.replace("1Key6", "S")
    inputKey7 = inputKey6.replace("1Key7", "D")
    inputKey8 = inputKey7.replace("1Key8", "F")
    inputKey9 = inputKey8.replace("1Key9", "G")
    
    notesList.append(inputKey9)
    timeList.append(currentNote["time"])

lasttime = 0
finalString = ""
temp = 0
for note in notesList:
    currentTime = timeList[temp]
    if(currentTime != lasttime):
        finalString += " "
    finalString += note
    lasttime = currentTime
    temp += 1

print(finalString)