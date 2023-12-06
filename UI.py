import tkinter as tk
from tkinter import *  
from tkinter import messagebox  
from words import words
import random
import subprocess
import sys

def generate_key_word():
    word, key = random.choice(list(words.items()))
    return word, key
def update():
    global key
    word, key = generate_key_word()
    # lbl = Label(window, text="Введите перевод слова - " + word) 
    # lbl.pack()
    lbl.config(text="Введите Столицу Страны - " + word)
    # txt = Entry(window,width=10) 
    # btn = Button(window, text="Узнать перевод(КЛИК)", command=clicked)  
    # btn.pack() 
    # txt.pack()
    # txt.config()

def restart():

   python = sys.executable
   subprocess.call([python, __file__])
   sys.exit()

def clicked():  
    res = format(txt.get()) 
    if res == key:
        messagebox.showinfo('Ответ:', 'Вы ответили правильно - ' + key)  
    else:
        messagebox.showerror("Ответ:", "Вы ошиблись!Столицей будет - " + key)
  
word, key = generate_key_word()
              
window = Tk()  
window.title("Тренажёр Стран и их Столиц - AlfredProgram")  
window.geometry('340x440')  
lbl = Label(window, text="Введите Столицу Страны - " + word) 
lbl.pack()
#lbl.grid(column=0, row=0) 
txt = Entry(window,width=10)  
txt.pack()
#txt.grid(column=1, row=0)  
btn = Button(window, text="Узнать Ответ(КЛИК)", command=clicked)  
btn.pack()
#btn.grid(column=0, row=1) 
btn = Button(window, text="Выдать новую Страну", command=update)  
btn.pack()
window.mainloop()