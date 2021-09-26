import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.149 Safari/537.36'
}

i = 0
n = 27820001915226
while i <= 24:
    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/" + str(n + i) + "/major/"
    data = requests.get(url, headers=headers).json()
    deputats_name = []
    deputats_voice = []
    for _ in data['report']['line'][18:]:
        deputats_voice.append(_['kolza'])
        deputats_name.append(_['txt'])
    print ("Результаты на ОИК №" + str(i+1) )
    l = len(deputats_name)
    j = 0
    while j < l:
        print(deputats_name[j] + ": " + deputats_voice[j])
        j += 1
    print()
    i += 1
