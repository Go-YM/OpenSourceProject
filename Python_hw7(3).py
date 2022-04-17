from tkinter import*
from tkinter import ttk

window=Tk()
baseTab=ttk.Notebook(window)
tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text='강아지')
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text='고양이')

##2019038003 고영민##

baseTab.pack(expand=1,fill="both")
photoDog=PhotoImage(file="C:/Users/고영민/Desktop/강아지.GIF")
labelDog=Label(tabDog,image=photoDog)
labelDog.pack()
photoCat=PhotoImage(file="C:/Users/고영민/Desktop/고양이.GIF")
labelCat=Label(tabCat,image=photoCat)
labelCat.pack()

window.mainloop()
