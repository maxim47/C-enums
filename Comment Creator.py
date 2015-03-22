import re
import os
os.chdir("C:/Users/Mark/Desktop")
enumsrd = open("enum.txt", "r")
text = enumsrd.read()
enums = open("enumnew.txt", "w")
stop = False

line = []
long = 1
new = 0
for letter in text:
    if letter is "\n":
        line = "".join(line)

        if re.search(",", line):
            for letters in line:
                if letters is not "/":
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

        elif re.search("NUMBER_OF_EVENTS$", line):
            for letters in line:
                if letters is not "/":
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

number = 0
line = []
for letter in text:
    current = 0
    final = 0
    if letter is "\n":
        line = "".join(line)
        for letters in line:
            if letters is not "/":
                if stop == False:
                    current += 1
            else:
                if stop == False:
                    stop = True
                else:
                    pass
        final = long - current
        stop = False
        
        if re.search(",", line):
            number += 1
            enums.write(line)
            if not re.search("//", line):
                for times in range(final):
                    enums.write(" ")
                enums.write("//")
            enums.write(" "+str(number))
            line = []
            line.append(letter)

        elif re.search("NUMBER_OF_EVENTS$", line):
            number += 1
            enums.write(line)
            if not re.search ("//", line):
                for times in range(final):
                    enums.write(" ")
                enums.write("//")
            enums.write(" "+str(number))
            line = []
            line.append(letter)

        else:
            enums.write(line+"\n")
            line = []

    else:
        line.append(letter)
enums.close()
enumsrd = open("enumnew.txt", "r")
print(enumsrd.read())

