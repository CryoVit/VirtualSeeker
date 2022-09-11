id = (434334701	,
480680646	,
7706705	,
14387072	,
480745939	,
420249427	,
666726801	,
741520	,
421267475	,
477342747	,
56748733	,
690608693	,
98181	,
690608704	,
690608687	,
477317922	,
529249	,
61639371	,
370687588	,
392505232	,
558070433	,
1750561	,
690608686	,
434401868	,
690608709	,
455916618	,
1484169431	,
666726799	,
6853766	,
474369808	,
472877684	,
628292885	,
690608706	,
477306079	,
666726803	,
558070436	,
690608691	,
490331391	,
690608690	,
690608698	,
480675481	,
1155425566	,
690608714	,
690608694	,
472845978	,
628292881	,
690608702	,
472821519	,
690608695	,
558070434	,
690608688	,
666726802	,
36795838	,
666726800	,
690608689	,
370689210	,
455965041	,
12485637	,
1405589619	,
690608712	,
176836079	,
690608696	,
370687372	,
322210278	,
1954091502	,
690608701	,
319810877	,
1116072703	,
690608692	,
690608711	,
1739085910	,
690608710	,
)

import requests
import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
fulldata = pd.DataFrame(columns = ['name', 'face'])

def getfile (bid):
    # url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(bid) + '&jsonp=jsonp'
    url = 'https://api.vtbs.moe/v1/detail/' + str(bid)
    r = requests.get(url)
    with open (str(bid) + 'i.json', mode = 'wb') as loaf:
        loaf.write(r.content)
        
def parsefile (bid):
    global fulldata
    with open (str(bid) + 'i.json', mode = 'rb') as loaf:
        ldict = json.load(loaf)
    # ldict = ldict['data']
    fulldata = fulldata.append({'name': ldict['uname'], 'face': ldict['face'][28:]}, ignore_index = True)

for i in range(0, 72):
    getfile(id[i])
    parsefile(id[i])
    print(i)

# with open('0i.txt', mode = 'w', encoding = 'utf-8') as loaf:
#     loaf.write(str(fulldata))

fulldata.to_csv('0i.csv', encoding = 'utf-8', index = False)
    