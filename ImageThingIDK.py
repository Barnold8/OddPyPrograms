from random import randint
import os

for i in range(int(input("How many random images do you want to see?"))):
  x1 = randint(0,9)
  x2 = randint(0,9)
  x3 = randint(0,9)
  x4 = randint(0,9)
  a = chr(randint(97,122))
  b = chr(randint(97,122))
  string = "start https://prnt.sc/{}{}{}{}{}{}".format(a,b,x1,x2,x3,x4)
  os.system(string)
  #print(string)
  


