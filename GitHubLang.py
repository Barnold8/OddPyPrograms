import requests
from bs4 import BeautifulSoup
import platform
import os
from random import randint
from collections import Counter


def validity(dataOBJ,site):
    
    if dataOBJ.status_code != 200:
        print("Cannot connect to Github, ensure you gave the correct link")
        return

    site_split = site.split(".")[0] if "www" not in site.lower() else site.split(".")[1]
    if "github" not in site_split.lower():
        print("Site entered was not github, you entered {}".format(site_split))
        return


def getPages(site_txt):
    pages = []
    scraping = True
    page = 1

    while scraping:

        site = requests.get("{}?page={}&tab=repositories".format(site_txt,page))
        soup = BeautifulSoup(site.text,features="lxml")
        for h in soup.find_all("h2",{"class": "blankslate-heading"}):#
            return pages # if any blankslate is found, end the scraping
        page = page + 1
        pages.append(soup)

    print("User has {} pages".format(page))

    return pages

def getRepos(site):

    links = []
    pages = getPages(site)

    for page in pages:
        for a in page.find_all("a",itemprop="name codeRepository"):
            links.append("https://github.com{}".format(a["href"]))
    return links

def getLangs(links):

    plat = platform.system()

    langs = []
    bar = "[" + " " * len(links) + "]"
    barlen = 1

    print("This may take a while...")
    for link in links:
        
        r = requests.get(link).text
        x = BeautifulSoup(r,features="lxml")
        
        f = list(bar)
        f[barlen] = "#"
        barlen = barlen + 1
        bar = ''.join(f)
    
        if plat.lower() == "windows":
            os.system("cls")
        else:
            os.system("clear")
        
        print("="*15 + " Just going through the repositories " + "="*15)
        print("\n\nProgess {}".format(bar))
        print("\n\n" + "="*(30+len(" Just going through the repositories ")))
        print("\n\n\t\tThis may take a while"+"."*randint(1,5))


        for s in x.find_all("li", {"class":"d-inline"}): #github please dont change your CSS classes i beg
            langs.append(s.text.strip().split("\n")[0])



    return langs


def main(): # basic main function

    site = input("Please input the github profile link you wish to process: ")
    data = requests.get(site)
    validity(data,site) # check to see if everything needed is valid
    langs = getLangs(getRepos(site))

    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")


    percents = Counter(langs)
    percents = [(i, percents[i] / len(langs) * 100.0) for i in percents]
    percents.sort(key=lambda tup: tup[1],reverse=True)
    for sets in percents:
        print(sets[0],": \t{:.2f}%".format(sets[1]))

        
main()