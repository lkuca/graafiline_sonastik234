from module3 import *
from tkinter import *
def veneaken():
    def teem_white():
        aken7["bg"]="white"
    def teema_black():
    
        aken7["bg"]="black"
    eesti_list =[] 
    vene_list=[] 
    vene_list=Loe_failist("vene.txt")
    eesti_list=Loe_failist("eesti.txt")
    aken7=Tk()
    aken7.geometry("900x500") 
    #t=""
    #for x in vene_list:
    #    t +=x+"\n"
    btn1=Button(aken7,text="перевести",font="Arial 24",relief=GROOVE,command=tõlkida1)
    btn5=Button(aken7,text="добавить слово",font="Arial 24",relief=GROOVE,command=lisa_sõna1)
    btn6=Button(aken7,text="исправить ошибку",font="Arial 24",relief=GROOVE,command=muuda_sona1)
    btr1=Button(aken7,text="черный",font="Arial 24",relief=GROOVE,command=teema_black)
    btr2=Button(aken7,text="белый",font="Arial 24",relief=GROOVE,command=teem_white)
    #btn.bind("Button-1",tõlkida)
    btn1.pack(anchor="ne")
    btn5.pack(anchor="ne")
    btn6.pack(anchor="ne")
    btr1.pack(anchor="ne")
    btr2.pack(anchor="ne")
    aken7.mainloop()
