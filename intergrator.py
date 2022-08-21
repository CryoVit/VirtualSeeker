import requests
import pandas as pd
import json

pd.set_option('display.max_rows', None)
fulldata = pd.DataFrame(columns =['uid', 'room_id', 'name', 'guard_num'])

def getfile (gid, page_size, file_path) :
    url = "https://api.live.bilibili.com/xlive/app-ucenter/v1/guard/Honor?target_id=0&gid="+str(gid)+"&area_id=9&page=1&page_size="+str(page_size)
    r = requests.get(url)
    with open(file_path, mode = 'wb') as loaf:
        loaf.write(r.content)

def parsefile (file_path):
    global fulldata
    with open(file_path, 'rb') as loaf:
        ldict = json.load(loaf)
    ldict = ldict['data']
    ldict = ldict['list']
    data = pd.DataFrame(ldict, columns =['uid', 'room_id', 'name', 'guard_num'])
    fulldata = pd.concat([fulldata, data])

date = '220821/'

getfile(241, 10, date + '0.json')
getfile(75, 100, date + '1.json')
getfile(76, 900, date + '2.json')

parsefile(date + '0.json')
parsefile(date + '1.json')
parsefile(date + '2.json')

with open(date + 'full.txt', mode = 'w', encoding = 'utf-8') as loaf:
    loaf.write(str(fulldata))