import re
import os
user = input("What is your user file")
enumsFile = input("Which enum file do you want to edit on your Desktop")
os.chdir("C:/Users/"+user+"/Desktop")
enumsrd = open(enumsFile, "r")
text = enumsrd.read()
enums = open(enumsFile+"_new.txt", "w")
stop = False

line = []
long = 0
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

incorrect = False
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
                stop = True
        final = long - current
        if incorrect == True:
            final += 1
            incorrect = False
        stop = False
        
        if re.search(",", line) or re.search("NUMBER_OF_EVENTS$", line):
            number += 1
            enums.write(line)
            if not re.search("//", line):
                for times in range(final):
                    enums.write(" ")
                enums.write("//")
            enums.write(" "+str(number))
            line = []
            line.append(letter)
            incorrect = True


        else:
            enums.write(line+"\n")
            line = []

    else:
        line.append(letter)
enums.close()
enumsrd = open(enumsFile+"_new.txt", "r")
print(enumsrd.read())

