import os


linkstr = ""
link = input("Please input the link: ")


for chars in link:

    if chars == '%':
        linkstr += "^"
    linkstr += chars

os.system("cls")
print("Link: {}".format(linkstr))