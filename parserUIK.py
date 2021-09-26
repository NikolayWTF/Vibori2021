import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.149 Safari/537.36'
}
i = 0
j = 0

while j < 32:
    a = 1
    vrn = 4784001269000 + i
    UIK = 4784001384349 + j

    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 10:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            deputats_name = []
            deputats_voice = []
            try:
                b = data['report']['line']
                for _ in data['report']['line'][18:]:
                    deputats_voice.append(_['kolza'])
                    deputats_name.append(_['txt'])
                print("Результаты на " + UIKnumber)
                l = len(deputats_name)
                index = 0
                while index < l:
                    print(deputats_name[index] + ": " + deputats_voice[index])
                    index += 1
                print()
                i = 0
                j += 1
            except KeyError:
                print("Информации по " + UIKnumber + " не было обнаруженно")
                print()
                i = 0
                j += 1
    else:
        print("Информации по УИК № " + str(j+1) + " не было обнаруженно")
        print()
        i = 0
        j += 1

i = 0
j = 0
while j < 28:
    a = 1
    vrn = 4784001269073 + i
    UIK = 478403191303 + j

    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/" + str(UIK) + "/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 10:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            deputats_name = []
            deputats_voice = []
            try:
                b = data['report']['line']
                for _ in data['report']['line'][18:]:
                    deputats_voice.append(_['kolza'])
                    deputats_name.append(_['txt'])
                print("Результаты на " + UIKnumber)
                l = len(deputats_name)
                index = 0
                while index < l:
                    print(deputats_name[index] + ": " + deputats_voice[index])
                    index += 1
                print()
                i = 0
                j += 1
            except KeyError:
                print("Информации по " + UIKnumber + " не было обнаруженно")
                print()
                i = 0
                j += 1
    else:
        print("Информации по УИК № " + str(j + 1) + " не было обнаруженно")
        print()
        i = 0
        j += 1

# первые 32 есть
#61