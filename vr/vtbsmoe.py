id = (480680646	,
434334701	,
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
import time

pd.set_option('display.max_rows', None)

def getfile (bid):
    url = "https://api.vtbs.moe/v2/bulkActive/"+str(bid)
    r = requests.get(url)
    with open(str(bid)+'.json', mode = 'wb') as loaf:
        loaf.write(r.content)

def parsefile (bid):
    with open(str(bid) + '.json', 'rb') as loaf:
        ldict = json.load(loaf)
        data = pd.DataFrame(ldict, columns =['time', 'follower'])
        newdata = pd.DataFrame(columns = ['date', str(bid)])
        # for idx, ln in data.iterrows():
        #     ln['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ln['time']) // 1000))
        #     data.iloc[idx] = ln
        # data.to_csv(str(bid) + '.csv', index = False)
        last_date = ''
        for idx, ln in data.iterrows():
            cur_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ln['time']) // 1000))
            ln['time'] = cur_str[0:10]
            data.iloc[idx] = ln
            if cur_str[8:10] != last_date:
                newdata.loc[len(newdata.index)] = [data.iloc[idx - 1]['time'], data.iloc[idx - 1]['follower']]
                last_date = cur_str[8:10]
        
        newdata.drop(newdata.index[0], inplace = True)
        # newdata.drop(newdata.index[len(newdata) - 1], inplace = True)
        # newdata.loc[data.iloc[len(data) - 1]['time']] = data.iloc[len(data) - 1]['follower']
        newdata.to_csv(str(bid) + 'r.csv', index = False)
            

for i in range(0, 72):
    getfile(id[i])
    parsefile(id[i])
    print(i)