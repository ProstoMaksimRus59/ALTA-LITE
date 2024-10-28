from urllib.error import URLError
import zipfile,keyboard,os,sys,re,shutil,urllib.request
print("Загрузка/обновление датабазы...")

#Настройка
url = 'https://drive.google.com/uc?export=download&id=1kgZ8K5OQJkP2WBoAfq-4n9ARHrfoeL-M' #откуда качать будет датабазу.

try:
    urllib.request.urlretrieve(url, "Base.zip")
    print("Успешно!\n")
except URLError:
    print("Ошибка.. автономный режим")
try:
    shutil.rmtree("Base")
except FileNotFoundError:
    print
try:
    zip = zipfile.ZipFile('Base.zip', 'r')
except FileNotFoundError:
    sys.exit()
zip.extractall('')
try:
    plar = open("plar.ALTAL", 'r')
except FileNotFoundError:
    plar = open("plar.ALTAL", 'w')
    print("Все игроки в базе")
    files = os.listdir("Base/")
    files = filter(lambda x: x.endswith('.altapl'), files)
    for plaer in files:
        fuckrstrip = plaer.split(".altapl")
        if plaer != "":
            print(fuckrstrip[0],end = " ; ")
    print("\n", end = "\n")
    com = input("Ваш ник>")
    test = 0
    files = os.listdir("Base/")
    files = filter(lambda x: x.endswith('.altapl'), files)
    for plaer in files:    
        fuckrstrip = plaer.split(".altapl")
        if fuckrstrip[0].lower() == com.lower(): 
            plar.write(com)
            test = 1
    if test == 0:
        print("Такого игрока нет в базе")
        input("")
        sys.exit()
    plar.close()
    plar = open("plar.ALTAL", 'r')
gdplar = plar.read()
plar.close()
def scanallvl(): #Ищет все лвла
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    lvls.append("")
    data.close()
    scan = "0"
    cout = 0
    alllvl = []
    alllvl.append(lvls[0].rstrip("\n"))
    while scan != "":
        if (cout % 8) == 0:
            alllvl.append(scan.rstrip("\n"))
        cout = cout + 1
        scan = lvls[cout]
    return alllvl

def infolvl(lvl,setmode):
    good = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    scan = 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == lvl.lower():
            info = 6
            while info != 0:
                info = info - 1
                lvlinfo = data.readline().rstrip('\n').lower()
                if setmode == "1":
                    print(lvlinfo)
                if info == 0:
                    return lvlinfo.split(":")[-1]
                scan = 1
                good = 1
        if lvlscan == "":
            scan = 1
    
    if good == 0:
        if setmode == "1":
            print("лвл не Найден в базе")
        return 0
    data.close()

def scanerpla(lvl,type):
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    cout = 0

    while lvls != "":
        try:
            if lvls[cout].split("\n")[0] == lvl:
                dl = lvls[cout + int(type)].split(":")[-1]
                return dl.rstrip('\n')
        except IndexError:
            return 0
        cout = cout + 1

def top(data,pp,target): #Делает топ
    datapp = ([])
    cont = 0
    for d in data:
        pp1 = float(pp[cont])
        datapp.append((d,pp1))
        cont = cont + 1
    datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
    cont = 1
    for printtop in datapp:
        if printtop[1] != 0:
                if target.lower() == printtop[0].lower():
                    print("топ-" + str(cont),end="\n")
                    return 1
                if target == "0":
                    print("Топ-" + str(cont))
                    print(" " + str(printtop[0]))
                    print(" pp:" + str(printtop[1]) + '\n')
        cont = cont + 1
def tophelper(plaer):
        
        hardest = 1 #по название доложно понятно быть)
        folder = "base/" + plaer.replace('"', '')
        file = open(folder, 'r')
        pp = 0
        Scan = 1
        plarr = []
        pparr = []
        plarr.append(file.readline().rstrip('\n')) #Показывает какой игрок
    
        while Scan == 1:
            pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
    
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
    
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1
    
            if lvl == 0:
                Scan = 0
                pparr.append(pp)
        return pparr
def plalvlcomm(requirements,lvl1):
            if requirements == "-ver": #если лвл
                alllvl = scanallvl() #Получает все лвла
                safelllvl = scanallvl()
                pplvl = []
                for lvl in safelllvl:
                    if scanerpla(lvl, '2') != "?":
                        pplvl.append(infolvl(lvl,"0")) #Получает пп
                    else:
                        alllvl.remove(lvl)
                try:
                    top(alllvl,pplvl,lvl1) #Делает топ
                except IndexError:
                    print("А их нет :/")
            if requirements == "-p":
                Ramdonmane = os.listdir("Base/") #ищет в базе игроков
                Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
                pplvl = []
                alllvl = []
                for plaer in Ramdonmane:
                    wfr = plaer.split(".altapl")
                    alllvl.append(wfr[0])
                    pplvl.append(round(tophelper(plaer)[0])) #Получает пп
                top(alllvl,pplvl,lvl1)#Делает топ
            if requirements == "-l": #если лвл
                alllvl = scanallvl() #Получает все лвла
                pplvl = []
                for lvl in alllvl:
                    pplvl.append(infolvl(lvl,"0")) #Получает пп
                top(alllvl,pplvl,lvl1) #Делает топ            
def infomain(pla):
    try:
        file = open("Base/"+str(pla) + ".altapl", 'r')
    except FileNotFoundError:
        plar.close()
        os.remove("plar.ALTAL")
        sys.exit()
    hardest = 1 #по название доложно понятно быть)
    pp = 0
    Scan = 1
    print("\n Player:" + file.readline().rstrip('\n'), end=" ") #Показывает какой игрок

    while Scan == 1:
            data = file.readline().rstrip('\n')
            pp1 = re.findall(r'\d+', data.rstrip(' ').rstrip('\n').rstrip(':'))
            if hardest == 1:
                hh = data
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1

            if lvl == 0:
                print("PP:" + str(round(pp)), end = " ")
                plalvlcomm("-p",pla)
                print(" Hardest>  " + str(hh) + "pp", end=" ")
                hh = hh.split(":")
                return hh[0]
print("\nALTA LITE v1.1(suport v4.0)")            
plalvlcomm("-ver",infomain(gdplar))

print("\nПосмотр топа игроков нажмите - 1")
print("Посмотр топа всех лвлов нажмите - 2")
print("Посмотр топа всех верифнутых лвлов нажмите - 3")
print("Посмотреть что вы прошли - 4")
print("Поменять игрока - 5(Перезапуск)")
print("Выход - 6")
com = 0
com2 = 0
while com != "6":
    com = keyboard.read_key()
    if com2 != com:
        match com:
            case "1":
                plalvlcomm("-p","0")
            case "2":
                plalvlcomm("-l","0")
            case "3":
                plalvlcomm("-ver","0")
            case "4":
                file = open("Base/"+str(gdplar) + ".altapl", 'r')
                file.readline()
                print("ЛВЛ ---- ПП")
                print(file.read())
                file.close()
            case "5":
                os.remove("plar.ALTAL")
                sys.exit()
    com2 = com
