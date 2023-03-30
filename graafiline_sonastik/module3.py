from pickle import LIST
from tkinter import *
import random
global vene_list, eesti_list
vene_list=[]
eesti_list=[]

def Loe_failist(fail:str)->list:
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def tõlkida1():
    vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    aken=Tk()
    aken.geometry("800x500")
    tran=Label(aken, text="видите то что хотите перевести:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
    translate=Entry(aken, text="Sisesta sõna mis tahad tõlkida:",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
    tran.pack()
    translate.pack()
    def tõlkida_check(event):
        trin=translate.get()
        if trin.lower()[0] in vene_letters:
            vast=Label(aken, text=f"{trin} на русском языке:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
            vast.pack()
            try:
                ind = vene_list.index(trin)
                vaste = eesti_list[ind]
                trun=Label(aken, text=trin+"-"+vaste,bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                trun.pack()
            except ValueError:
                tron=Label(aken, text=f"слово не найдено",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                tron.pack()
        else:
            k=Label(aken, text=f"{trin} на эстонском",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
            k.pack()
            try:
                ind =eesti_list.index(trin)
                vaste = vene_list[ind] 
                v=Label(aken, text=f"{trin} - {vaste}",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                v.pack()
            except ValueError:
               tron1=Label(aken, text=f"слово не найдено",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
               tron1.pack()
    aken.bind("<Return>",tõlkida_check)
    aken.mainloop()
def Kirjuta_failisse(fail:str,sona:str):
    f=open(fail,"a",encoding="utf-8-sig")
    f.write(sona+"\n")
    f.close()
def lisa_sõna1():
    aken1=Tk()
    aken1.geometry("800x500")
    u=Label(aken1, text="добавь русское слово:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
    uussona=Entry(aken1, text="lisa vene sona:",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
    u.pack()
    uussona.pack()
    def sona_check(event):
        l= uussona.get()
        t=Label(aken1, text="переведи это слово:",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
        translate=Entry(aken1, text="tolgi seda sona:",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
        t.pack()
        translate.pack()
        def sona_check2(event):
            b=translate.get()
            vene_list.append(l)
            eesti_list.append(b)
            Kirjuta_failisse("vene.txt",l)
            Kirjuta_failisse("eesti.txt",b)
            g=Label(aken1, text="слово дабавлено, попробуй перевести!",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
            g.pack()
        aken1.bind("<Return>",sona_check2)    
    aken1.bind("<Return>",sona_check)
    aken1.mainloop()
def muuda_sona1():
    aken2=Tk()
    aken2.geometry("800x500")
    x=Label(aken2, text="старое слово на русском языке: ",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
    x2=Entry(aken2, text="vana sõna: ",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
    x.pack()
    x2.pack()
    def continus(event):
        klamb=x2.get()
        if klamb in vene_list:
            y=Label(aken2, text="новое слово на русском языке: ",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
            y2=Entry(aken2, text="uus sõna: ",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
            y.pack()
            y2.pack()
            def continus2(event):
                klimb=y2.get()
                ind=vene_list.index(klamb) 
                vene_list.remove(klamb) 
                vene_list.insert(ind,klimb)

                k=Label(aken2, text=f"переведи {klimb}: ",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                k2=Entry(aken2, text=f"translate {klimb}: ",bg="silver",fg="#AA4A44",font="Arial 20",width=55)
                k.pack()
                k2.pack()
                def continus3(event):
                    klumb=k2.get()
                    eesti_list.pop(ind)
                    eesti_list.insert(ind,klumb) 

                    f=open("vene.txt","w",encoding="utf-8-sig")
                    for sona in vene_list:
                        f.write(sona+"\n")
                    f=open("eesti.txt","w",encoding="utf-8-sig")
                    for sona in eesti_list:
                        f.write(sona+"\n")
                    m=Label(aken2, text="слово изменено",bg="silver",fg="#AA4A44",font="Arial 20",height=1,width=55)
                    m.pack()
                aken2.bind("<Return>",continus3) 
            aken2.bind("<Return>",continus2)
    aken2.bind("<Return>",continus)




vene_list=Loe_failist("vene.txt")
eesti_list=Loe_failist("eesti.txt")

