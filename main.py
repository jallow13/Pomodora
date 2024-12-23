import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
res = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    screen.after_cancel(res)
    canvas.itemconfig(count_text,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
    text.config(text="Timer",fg=GREEN,bg=YELLOW, font=(FONT_NAME,32,"bold"))
    label.config(text=" ",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    work=WORK_MIN *60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        text.config(text="Break",fg=RED)
        count_down(long_break)
    elif  reps % 2 ==0:
        text.config(text="Break",fg=PINK)
        count_down(short_break)
    else:
        text.config(text="Work")
        count_down(work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(count_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global res
        res = screen.after(1000,count_down,count - 1)
    else:
        start_count()
        marks =""
        marks_t = math.floor(reps / 2)
        for _ in range(marks_t):
            marks += "✔"
        label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

screen=Tk()
screen.title("Pomodoro")
screen.config(padx=120,pady=50,bg=YELLOW)





canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_pic = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image_pic)
count_text = canvas.create_text(100,120,text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(row=1,column=1)

text=Label(text="Timer",fg=GREEN,bg=YELLOW, font=(FONT_NAME,32,"bold"))
text.grid(row=0,column=1)

start_btn=Button(text="Start",highlightthickness=0,command=start_count)
start_btn.grid(row=3,column=0)

button2=Button(text="Reset",highlightthickness=0,command=reset_time)
button2.grid(row=3,column=3)

label = Label(text=" ",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
label.grid(row=4,column=1)


screen.mainloop()