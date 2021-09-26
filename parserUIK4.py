import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/80.0.3987.149 Safari/537.36'
}
i = 0
j = 0

while j < 28:
    a = 1
    vrn = 4784002285000 + i
    UIK = 478403382216 + j

    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 1000:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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

while j < 26:
    a = 1
    vrn = 4784002285000 + i
    UIK = 478403283755 + j

    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 1000:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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

while j < 22:
    a = 1
    vrn = 4784002285000 + i
    UIK = 4784002402086 + j


    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 1000:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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

while j < 2:
    a = 1
    vrn = 4784002181631 + i
    UIK = 478403283781 + j


    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 369:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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
j = 0
while j < 1:
    a = 1
    vrn = 4784002218885 + i
    UIK = 4784002402108 + j


    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 369:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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

j = 0
i = 0
while j < 1:
    a = 1
    vrn = 4784002289072 + i
    UIK = 478403283783 + j


    url = "http://cikrf.ru/iservices/sgo-visual-rest/vibory/27820001915220/results/"+str(UIK)+"/major/?vrnkomis=" + str(vrn)
    try:
        data = requests.get(url, headers=headers).json()
    except BaseException:
        a = 0
    if i < 369:
        if a == 0:
            i += 1
        else:

            UIKnumber = data['report']['tvd']
            name = []
            result = []
            try:
                b = data['report']['line']
                ind = 0
                for _ in data['report']['line']:
                    if (ind == 17):
                        ind += 1
                    else:
                        name.append(_['txt'])
                        result.append(_['kolza'])
                        ind += 1
                print("Результаты на " + UIKnumber)
                l = len(name)
                index = 0
                while index < l:
                    print(name[index] + " " + result[index])
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

#104-183
#131-157-183
