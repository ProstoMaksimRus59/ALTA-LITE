import os
import re
import shutil
import sys
from tkinter import *
from tkinter import scrolledtext
from tkinter.messagebox import showerror, showinfo
from urllib.error import URLError
import zipfile,os,sys,re,shutil,urllib.request

#Для нормального запуска надо создать ico(128x128) и png(680x720) и назвать так AL.ico(иконка на проге) и AL_BG.png(Фон)
# Еще они доложны быть в папке "Resources"
#
#
showinfo(title="Загрузка датабазы", message="Подождите,\nAlta сразу запусится после загрузки датабазы.")
url = 'https://drive.google.com/uc?export=download&id=1kgZ8K5OQJkP2WBoAfq-4n9ARHrfoeL-M' #откуда качать будет датабазу.(тут пример ссылки)
try:
    urllib.request.urlretrieve(url, "Base.zip")
    print("Успешно!\n")
except URLError:
    print("Ошибка.. автономный режим")
    showerror(title="Ошибка..", message="Нет связи с датабазой,\n(зпущен автономный режим)")
root = Tk()
root.title("ALTA LITE v2.0 (suport v4.0)")
root.geometry("680x720")
root.resizable(False,False)
root.iconbitmap(r'Resources\\AL.ico')
root["bg"] = 'gray'
print("консоль закладки))")
no = 0
print("Загрузка/обновление датабазы...")
try:
    autocheck = open("plar.ALTAL", 'r')
    autoplar = autocheck.read()
    autocheck.close()
except FileNotFoundError:
     no = 1
#Настройка
 
try:
    shutil.rmtree("Base")
except FileNotFoundError:
    print
try:
    zip = zipfile.ZipFile('Base.zip', 'r')
except FileNotFoundError:
    sys.exit()
zip.extractall('')

def beat():
    name = textok['text']
    if name == "Пусто" or name == "Такого игрока нет базе":
        textout = Label(text = "<Ник нормальный сюда веди",font="Impact 15",anchor='nw',)
        textout.place(y = 30, x = 370,width=300,height=680)
        textoutt.delete(0, END)
        textoutt.insert(0,"<Ник нормальный сюда веди")
        textouto.delete(0, END)
        textouto.insert(0,"<Ник нормальный сюда веди")
        return 0
    file = open("Base/"+str(name) + ".altapl", 'r')
    file.readline()
    print("ЛВЛ ---- ПП")
    beatt = file.read()
    print(beatt)
    file.close()
    textout = Label(text = beatt,font="Impact 10",anchor='n')
    textout.place(y = 30, x = 370,width=300,height=680)
    textoutt.delete(0, END)
    textoutt.insert(0,beatt)
    textouto.delete(0, END)
    textouto.insert(0,beatt)

def top(data,pp,target): #Делает топ
    superdata = []
    datapp = ([])
    cont = 0
    for d in data:
        pp1 = float(pp[cont])
        datapp.append((d,pp1))
        cont = cont + 1
    datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
    cont = 1
    for printtop in datapp:
        print(printtop)
        if printtop[1] != 0:
                if target.lower() == printtop[0].lower():
                    superdata.append("топ-" + str(cont),end="\n")
                    return 1
                if target == "0":
                    superdata.append("Топ-" + str(cont))
                    superdata.append(" " + str(printtop[0]))
                    superdata.append("\n pp:" + str(printtop[1]) + '\n')
        cont = cont + 1
    return superdata

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

def nikttop(name):
                Ramdonmane = os.listdir("Base/") #ищет в базе игроков
                Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
                pplvl = []
                alllvl = []
                for plaer in Ramdonmane:
                    wfr = plaer.split(".altapl")
                    alllvl.append(wfr[0])
                    pplvl.append(round(tophelper(plaer)[0]))
                print(pplvl)
                print(alllvl) 
                datapp = ([])
                cont = 0
                for d in alllvl:
                    pp1 = float(pplvl[cont])
                    datapp.append((d,pp1))
                    cont = cont + 1
                datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
                print(datapp)
                cout = 0
                for toper in datapp:
                    print(toper[0])
                    cout = cout + 1
                    if toper[0].lower() == name:
                        return cout
def toperlvl(name):
                alllvl = scanallvl() #Получает все лвла
                safelllvl = scanallvl()
                pplvl = []
                for lvl in safelllvl:
                    if scanerpla(lvl, '2') != "?":
                        pplvl.append(infolvl(lvl,"0")) #Получает пп
                    else:
                        alllvl.remove(lvl)
                datapp = ([])
                cont = 0
                for d in alllvl:
                    pp1 = float(pplvl[cont])
                    datapp.append((d,pp1))
                    cont = cont + 1
                datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
                print(datapp)
                cout = 0
                for toper in datapp:
                    print(toper[0])
                    cout = cout + 1
                    if toper[0].lower() == name:
                        return cout
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
            print(pp1)
            print("\\//")
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
    
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1
    
            if lvl == 0:
                Scan = 0
                pparr.append(pp)
        return pparr

def sttus(Name):
    files = open("base/"+ Name + ".altapl")
    files.readline()
    hardest1 = files.readline().split(":")
    files.close()
    try:
        file = open("Base/" + Name + ".altapl", 'r')
        file.readline()
    except FileNotFoundError:
        sys.exit()
    hardest = 1 #по название доложно понятно быть)
    pp = 0
    Scan = 1
    while Scan == 1:
            data = file.readline().rstrip('\n')
            print(data)
            pp1 = re.findall(r'\d+', data.rstrip(' ').rstrip('\n').rstrip(':'))
            if hardest == 1:
                hh = data
            print("ggg")
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1

            if lvl == 0:
                print(pp)
                out = ["Player:" + Name + " pp:" + str(round(pp)) +"\ntop:"+ str(nikttop(Name)) + "\nHardest:" + hardest1[0] + " pp:" + hardest1[1] + "top:" + str(toperlvl(hardest1[0]))]
                stus = Label(root,
                        text = ''.join(out)
                        ,font="Ariral 10"
                        ,anchor='n'
                        )
                stus.place(x=15, y=610,width=330,height=100)
                return 1

def toppla():
    Ramdonmane = os.listdir("Base/") #ищет в базе игроков
    Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
    pplvl = []
    alllvl = []
    for plaer in Ramdonmane:
        wfr = plaer.split(".altapl")
        alllvl.append(wfr[0])
        pplvl.append(round(tophelper(plaer)[0])) #Получает пп
    dad = top(alllvl,pplvl,"0")
    print(dad)
    textout = Label(
             text = ''.join(dad)
             ,font="Impact 10"
             ,anchor='n'
             )
    textout.place(y = 30, x = 370,width=300,height=680)
    textoutt.delete(0, END)
    textoutt.insert(0,''.join(dad))
    textouto.delete(0, END)
    textouto.insert(0,''.join(dad))
def toplvl():
    alllvl = scanallvl() #Получает все лвла
    pplvl = []
    for lvl in alllvl:
        pplvl.append(infolvl(lvl,"0")) #Получает пп
    dad = top(alllvl,pplvl,"0")
    print(dad)
    textout = Label(root
             ,text = ''.join(dad)
             ,font="Impact 10"
             ,anchor='n'
             )
    textoutt.delete(0, END)
    textoutt.insert(0,''.join(dad))
    textouto.delete(0, END)
    textouto.insert(0,''.join(dad))
    textout.place(y = 30, x = 370,width=300,height=680)

def up():
     downsrol = textoutt.get()
     fullsrol = textouto.get()
     
     dd = len(downsrol)
     du = len(fullsrol)
     print(str(du) + " s " + str(dd))
     target = du - dd
     print(target)
     textout = Label(root
             ,text = ''.join(fullsrol)
             ,font="Impact 10"
             ,anchor='n')
     textout.place(y = 30, x = 370,width=300,height=680)
     textoutt.delete(0, END)
     textoutt.insert(0,''.join(fullsrol))
     while target > 53:
          target = target - 68
          down()
def down():
    print("ориг")
    print(textoutt.get())
    srrol = textoutt.get().rsplit(':')
    srrol.pop(0)
    srrol.pop(0)
    print("обрезка")
    print(srrol)
    full = []
    counet = 0
    for sporka in srrol:
         if sporka != "":
            full.append(sporka + ":")
            print(full)
            counet = counet + 1
    print("Рель")
    print(''.join(full))
    if counet > 7:
        textout = Label(root
             ,text = ''.join(full)
             ,font="Impact 10"
             ,anchor='n')
        textout.place(y = 30, x = 370,width=300,height=680)
        textoutt.delete(0, END)
        textoutt.insert(0,''.join(full))
def topver():
    alllvl = scanallvl() #Получает все лвла
    safelllvl = scanallvl()
    pplvl = []
    for lvl in safelllvl:
        if scanerpla(lvl, '2') != "?":
            pplvl.append(infolvl(lvl,"0")) #Получает пп
        else:
            alllvl.remove(lvl)
    dad = top(alllvl,pplvl,"0")
    print(dad)
    textout = Label(
             text = ''.join(dad)
             ,font="Impact 10"
             ,anchor='n'
             )
    textout.place(y = 30, x = 370,width=300,height=680)
    textoutt.delete(0, END)
    textoutt.insert(0,''.join(dad))
    textouto.delete(0, END)
    textouto.insert(0,''.join(dad))
img = PhotoImage(file ='Resources\\AL_BG.png')
L_logo = Label(root, image=img )
L_logo.pack()
def deat():
    files = os.listdir("Base/")
    print(files)
    files = filter(lambda x: x.endswith('.altapl'), files)
    yname = name.get().lower()
    print(yname + " поиск")
    for plaer in files:    
        fuckrstrip = plaer.split(".altapl")
        print(fuckrstrip[0].lower())
        if yname == fuckrstrip[0].lower(): 
            textok["text"] = name.get().lower()
            setting = open("plar.ALTAL", 'w')
            setting.write(name.get().lower())
            setting.close()
            print(name.get().lower())
            print("gggggg")
            sttus(name.get().lower())
            print("Найден")
            return 1
        else:
            textok["text"] = "Такого игрока нет базе"
            stus = Label(root,
                 text = "..."
                ,font="Ariral 10"
                ,anchor='n'
                )
            stus.place(x=15, y=610,width=330,height=100)

e5 = Button(root,
           text= "\/"
           ,command = down
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )

textout = Label(
         text = "..."
         ,font="Impact 20"
         )
textout.place(y = 30, x = 370,width=300,height=680)
text = Label(root,
             text = "\\/Ник\\/ Сюда пиши  \\/Ник\\/"
             ,font="Impact 20"
             )
text.place(y = 0, x = 0)
e = Button(root,
           text= "Это я"
           ,command = deat
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )
e.place(x=10, y=100)
textok = Label(root
             ,font="Ariral 10"
             ,text = "Пусто"
             )
textok.place(x= 100 , y = 100,width=250)
name = Entry(font="Ariral 18")
textoutt = Entry(font="Ariral 18")
textouto = Entry(font="Ariral 18")
name.place(x=5, y=45,height=50,width=350)
e1 = Button(root,
           text= "Топ игроков"
           ,command = toppla
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )

e1.place(x=100, y=140, width=250)
e2 = Button(root,
           text= "Топ (ver) лвлов"
           ,command = topver
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )

e2.place(x=100, y=220, width=250)
e3 = Button(root,
           text= "Топ (всех) лвлов"
           ,command = toplvl
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )

e3.place(x=100, y=300, width=250)
e4 = Button(root,
           text= "Что вы прошли"
           ,command = beat
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )

e5 = Button(root,
           text= "\/"
           ,command = down
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )
e5.place(x=335, y=545, width=35)
e6 = Button(root,
           text= "/\\"
           ,command = up
           ,font="Impact 20"
           ,bg = 'white'
           ,activebackground="gray"
           ,activeforeground="white"
           )
e6.place(x=335, y=460, width=35)
e4.place(x=100, y=380, width=250)
stus = Label(font="Ariral 10",text = "...")

stus.place(x=15, y=610,width=330,height=100)
if no == 0:
    textok['text'] = autoplar
    sttus(autoplar)
root.mainloop()