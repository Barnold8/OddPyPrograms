# A program to auto shutdown the PC when a download is complete by using download speeds to guesstimate a time to shutdown the system
# You can use -M at the end of the command to force Megabyte per second and not megabit

import os
import sys
import datetime

def isFloat(string):

    x = "0123456789."

    for elem in string:
        if elem not in x:
            return False
    return True

def checks():

    x = False

    if len(sys.argv) < 3:
        
        print("This program needs: [average download speed (Megabit)] [size (in GB)] to run and you gave the following command:\n")
        s = ""
        for elem in sys.argv:
            s += "{} ".format(elem)
        
        print(s + "\n")
        exit()
 
    elif not isFloat(sys.argv[1]) or not isFloat(sys.argv[2]):
    
        print("Either the first or second parameter is not a number.")
        print("This program needs: [average download speed (Megabit)] [size (in GB)] to run and you gave the following command:\n")
        s = ""
        for elem in sys.argv:
            s += "{} ".format(elem)
        
        print(s + "\n")
        exit()

    elif len(sys.argv) == 4 and sys.argv[3].lower() == "-m":
        x = True
    
    return x


def GB2MB(): # GB -> MB
    return float(sys.argv[2]) * 1000 + 24 * float(sys.argv[2])

def MBPS2MB(): # MBPS -> MB
    return float(sys.argv[2]) * 0.125

def seconds2mins(time):
    return time / 60

def main():

    m_byte = checks()

    s = GB2MB() / float(sys.argv[1]) if m_byte else GB2MB() /  MBPS2MB() 
    t = str(datetime.timedelta(seconds=s))
    
    if os.name == "nt":

        os.system("shutdown -s -t {}".format(s))

    else:
        os.system("sudo shutdown +{}".format(int(seconds2mins(s))))

main()

