import os

link = input("Input the relative file path please. Including the file.\n\nExample: Desktop/Files/something.txt\n")
x = [] # make x global
allowed = ["http","https","www","com","net"]

try:
    with open(link) as file:
        x = file.readlines()
except IOError:
    print("File and/or path does not exist")
    exit()

for i in range(len(x)):
    x[i] = x[i].strip()
    
    for y in range(len(allowed)):
        if allowed[y] in x[i]:
            os.system(f"start {x[i]}".format())
            break
        



