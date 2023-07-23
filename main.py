
import time
import tkinter
import math

with open('samples.txt', 'r') as file:
    data = file.read()

start_time = "01:00"
session_time = 60  

#---------------functions--------------#

def main(session_time):
    if start():
        count_down(session_time)
    else:
      window.after(100,main,session_time)

def start():
    if len(type_input.get('1.0','end-1c')) > 0:
        return True

def count_down(count):
    count_min = divmod(count,60)[0]
    count_sec = divmod(count,60)[1]
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_text.config(text=f'{count_min}:{count_sec}')
    if count == 0:
        speed_calculate()
    if count > 0:
        window.after(1000,count_down,count-1)

def speed_calculate():
    num_correct_word = count_correct_word()
    word_per_min = num_correct_word / (math.floor(session_time / 60)) 
    canvas.itemconfig(sample_text,text =f'your type speed is : {word_per_min} Word/m')

def count_correct_word():
    words = data.lower().split()
    user_words = type_input.get('1.0','end-1c').split()
    correct_word = 0
    for i in range(len(user_words)):
        if words[i] == user_words[i]:
            correct_word += 1
    return correct_word


#-------------UI--------------

window = tkinter.Tk()

window.title('Type Speed Test')
window.minsize(width=800,height=600)
window.config(padx=50,pady=50)

canvas = tkinter.Canvas(width=650,height=400,bg='gray')
sample_text = canvas.create_text(325,200,text=data,font=("Time New Roman", 16),fill='white',width=500)

timer_text = tkinter.Label(text=start_time,font=("Time New Roman", 16))
timer_text.grid(column=0,row=0)

canvas.grid(column=0,row=1)
type_input = tkinter.Text(window,width=81,height=10)
type_input.grid(column=0,row=2,pady=20)


window.after(100,main,session_time)


window.mainloop()
