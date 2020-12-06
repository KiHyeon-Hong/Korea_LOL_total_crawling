from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import json
import sys

def _main_():
    html = requests.get('https://www.op.gg/summoner/userName=' + sys.argv[1])

    soup = bs(html.text, 'html.parser')
    board = soup.findAll('div',{'class':'KDA'})

    KDAs = []
    for i in range(0, len(board)):
        if(board[i].find('div',{'class':'KDA'})):
            KDAs.append(board[i].find('div',{'class':'KDA'}))

    kills = []
    deaths = []
    assists = []

    for i in range(0, len(KDAs)):
        kills.append((KDAs[i].find('span',{'class':'Kill'})).text)
        deaths.append((KDAs[i].find('span',{'class':'Death'})).text)
        assists.append((KDAs[i].find('span',{'class':'Assist'})).text)

    date = {

    }


    f = open("../files/test.txt", 'w')
    f.write(str(kills[0] + ',' + deaths[0] + ',' + assists[0]))
    f.close()

_main_()
