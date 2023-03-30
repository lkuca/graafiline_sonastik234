from module1 import *
from module2 import *
from tkinter import *
def teem_white():
    aken["bg"]="white"
def teema_black():
    aken["bg"]="black"
global laused
eesti_list =[] 
vene_list=[] 
vene_list=Loe_failist("vene.txt")
eesti_list=Loe_failist("eesti.txt")
aken=Tk()
aken.geometry("900x500") 
#aken.iconbitmap("badfavicon.ico")
photo = PhotoImage(file="ico.png")
p=Label(aken,image=photo)
aken.wm_iconphoto(True, photo)
aken.title("sonaraamat")
#t=""
#for x in vene_list:
#    t +=x+"\n"
btn=Button(text="tõlkida",font="Arial 24",relief=GROOVE,command=tõlkida)
btn2=Button(text="lisa sõna",font="Arial 24",relief=GROOVE,command=lisa_sõna)
btn3=Button(text="paranda viga",font="Arial 24",relief=GROOVE,command=muuda_sona)
btn4=Button(text="vene aken",font="Arial 24",relief=GROOVE,command=veneaken)
btn8=Button(text="valge ",font="Arial 24",relief=GROOVE,command=teem_white)
btn0=Button(text="must",font="Arial 24",relief=GROOVE,command=teema_black)
#btn.bind("Button-1",tõlkida)
p.pack()
btn.pack(anchor="ne")
btn2.pack(anchor="ne")
btn3.pack(anchor="ne")
btn4.pack(anchor="ne")
btn8.pack(anchor="ne")
btn0.pack(anchor="ne")
aken.mainloop()

