from tkinter import *  
from tkinter import messagebox  
from words import words
import random

def clicked():  
    if res == key:
        messagebox.showinfo('Ответ:', 'Вы ответили правильно - ' + key)  
    else:
        messagebox.showerror("Ответ:", "Вы ошиблись!Перводом будет слово - " + key)

word, key = random.choice(list(words.items()))
  
window = Tk()  
window.title("Тренажёр Английских слов (стран) AlfredProgram")  
window.geometry('400x250')  
lbl = Label(window, text="Введите перевод слова - " + word) 
lbl.grid(column=0, row=0) 
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Узнать перевод(КЛИК)", command=clicked)  
btn.grid(column=2, row=0)  
window.mainloop()