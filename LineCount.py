import sys
import re
import os
file = sys.argv[1]
enumsrd = open(file, "r")
text = enumsrd.read()
print(text)
enums = open("new"+file, "w")
stop = False
lastLine = str('NUMBER_OF_EVENTS$')

line = []
long = 0
new = 0
for letter in text:
    if letter is str('\n'):
        line = ''.join(line)

        if re.search(',', line):
            for letters in line:
                if letters is not str('/'):
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

        elif re.search(lastLine, line):
            for letters in line:
                if letters is not str('/'):
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
number = 0
line = []
for letter in text:
    current = 0
    final = 0
    if letter is str('\n'):
        line = ''.join(line)
        for letters in line:
            if letters is not str('/'):
                if stop == False:
                    current += 1
            else:
                stop = True
        final = long - current
        if incorrect == True:
            final += 1
            incorrect = False
        stop = False
        
        if re.search(str(','), line) or re.search(lastLine, line):
            number += 1
            enums.write(line)
            if not re.search(str('//'), line):
                for times in range(final):
                    enums.write(' ')
                enums.write(str('//'))
            enums.write(' '+str(number))
            line = []
            line.append(letter)
            incorrect = True


        else:
            enums.write(line+str('\n'))
            line = []

    else:
        line.append(letter)
enums.close()
enumsrd = open("new"+file, "r")
print(enumsrd.read())

