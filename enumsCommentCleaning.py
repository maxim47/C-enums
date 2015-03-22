import re
import os
os.chdir("C:/Users/Mark/Desktop")
enumsrd = open("enum.txt", "r")
text = enumsrd.read()
enums = open("enumnew.txt", "w")
global stop
stop = False

def details():
    global new
    global letters
    global line
    global long
    line = []
    long = 1
    new = 0
    for letter in text:
        if letter is "\n":
            line = "".join(line)

            if re.search(",", line):
                newLong(long)

            elif re.search("NUMBER_OF_EVENTS$", line):
                newLong(long)

            else:
                pass
            line = []
            new = 0
            
        else:
            line.append(letter)

def Main():
    global letters
    global stop
    global final
    global letter
    global line
    global long
    global number
    details()
    number = 0
    line = []
    for letter in text:
        current = 0
        final = 0
        if letter is "\n":
            line = "".join(line)
            for letters in line:
                Checkout(current)
            final = long - current
            stop = False
        
            if re.search(",", line):
                appending()

            elif re.search("NUMBER_OF_EVENTS$", line):
                appending()

            else:
                enums.write(line+"\n")
                line = []

        else:
            line.append(letter)

def Checkout(byte):
    global letters
    global long
    global line
    global stop
    
    if letters is not "/":
        if stop == False:
            byte += 1
    else:
        if stop == False:
            stop = True
        else:
            pass
    return byte

def appending():
    global final
    global letter
    global line
    global number
    number += 1
    enums.write(line)
    if not re.search ("//", line):
        for times in range(final):
            enums.write(" ")
        enums.write("//")
    enums.write(" "+str(number))
    line = []
    line.append(letter)

def newLong(old):
    global line
    global letters
    global new
    global stop
    for letters in line:
        Checkout(new)
        if new>old:
            old = new
    stop = False
    return old


Main()
enums.close()
enumsrd = open("enumnew.txt", "r")
print(enumsrd.read())

