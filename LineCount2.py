import sys
import re
import os
file = sys.argv[1]
enumsrd = open(file, "r")
text = enumsrd.read()
print(text)
enums = open("new"+file, "w")
stop = False
stop2 = False

line = []
long = 0
new = 0
number = 0
for letter in text:
    if letter == "\n":
        line = ''.join(line)

        if re.search(',', line):
            for letters in line:
                if letters != ("/"):
                    if stop == False:
                        new += 1
                else:
                    if stop == False:
                        stop = True
                    else:
                        pass
            if new>long:
                long = new
            stop = False

        else:
            pass
        line = []
        new = 0
            
    else:
        line.append(letter)

incorrect = False
line = []
for letter in text:
    current = 0
    final = 0
    if letter == "\n":
        line = ''.join(line)
        for letters in line:
            if letters != "/":
                if stop == False:
                    current += 1
            else:
                stop = True
        final = long - current
        if incorrect == True:
            final += 1
            incorrect = False
        stop = False
        
        if re.search((","), line):
            number += 1
            enums.write(line)
            if not re.search(("//"), line):
                for times in range(final):
                    enums.write(' ')
                enums.write(("//"))
                enums.write(" "+str(number))
            
            line = []
            line.append(letter)
            incorrect = True


        else:
            enums.write(line+str('\n'))
            line = []

    else:
        if letter != ("/"):
            if stop2 == False:
                line.append(letter)
        else:
            if stop2 == False:
                stop2 = True
                line.append(letter)
            else:
                line.append(letter)
                number += 1           
                line.append(" "+str(number))
                number -= 1
                stop2 = False

enums.close()
enumsrd = open("new"+file, "r")
print(enumsrd.read())

