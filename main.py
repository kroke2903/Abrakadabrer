from tkinter import *
from tkinter import ttk
import pyperclip as pc
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'Abrakadabrer_icon.ico')           # добавляем к этому пути имя файла

def clicked():
    fraze = txt.get()
    itog = []
    eng = list(
        "f , d u l t ` ; p b q r k v y j g h c n e a [ w x i o m s ] ' . z F < D U L T ~ : P B Q R K V Y J G H C N E A { W X I O M S } \"  > Z ! @ # $ % ^ & * ( ) / ?".split())
    rus = list(
        "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ь ы ъ э ю я А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ь Ы Ъ Э Ю Я ! \"  № ; % : ? * ( ) . ,".split())
    while len(fraze) > 0:
        if fraze[0] in eng:
            itog.append(rus[eng.index(fraze[0])])
            fraze = fraze[1:]
        elif fraze[0] in rus:
            itog.append(eng[rus.index(fraze[0])])
            fraze = fraze[1:]
        else:
            itog.append(fraze[0])
            fraze = fraze[1:]
    itg.configure(text=str(''.join(itog)))
    pc.copy(str(''.join(itog)))
    info = Label(root, text="Переведено... Скопировано в буфер.", bg='gray')
    info.pack(fill=BOTH, expand=True)


root = Tk()
root.iconbitmap(file_path)
root.title('Abrakadabrer v 1.01')
root.geometry('400x120')
lbl = Label(root, text="Введи свою Абру-кадабру...")
lbl.pack(fill=BOTH, expand=True)
txt = Entry(root)
txt.pack(fill=BOTH, expand=True)
ttk.Button(root, text='Перевести на человеческий', width=200, command=clicked).pack()
itg = Label(root, text='')
itg.pack(fill=BOTH, expand=True)
root.mainloop()