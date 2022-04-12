## Hex to RGB

def HEX2RGB(col):
    sections = []
    f = ""
    for i in range(len(col)):
        if i % 2 == 0 and i != 0:
            sections.append(f)
            f = ""
        f = f + col[i]
    sections.append(f)
    for i in range(len(sections)):
        sections[i] = int(sections[i],16)
    return sections

print("="*32)
print("Type exit to end the program")
print("="*32)
running = True
x = input("Input a Hex value\t")

while(running):
    if(x.lower() == "exit"):
        running = False
        break
    else:
        print(HEX2RGB(x))
        x =  input("Input a Hex value\t")


