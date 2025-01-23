from tkinter import *
import math
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
text="√"
check_count = 0
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global check_count,reps,timer
    window.after_cancel(timer)
    canvas.itemconfig(text_item,text="00:00")
    timer_label.config(text="Timer")
    check_count = reps = 0
    check_label.config(text=text * reps)
    timer = None

def reset_button():
    reset()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_countdown():
    global check_count
    global reps
    check_count += 1

    if check_count % 8 == 0:
        timer_label.config(text="Take Rest", font=(FONT_NAME, 35, "bold"), fg=RED, highlightthickness=0, bg=YELLOW)
        count_down(LONG_BREAK_MIN*60)
        return

    elif check_count % 2 == 0:
        timer_label.config(text="Take a Break", font=(FONT_NAME, 35, "bold"), fg=PINK, highlightthickness=0, bg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)

    else:
        timer_label.config(text="Working Time", font=(FONT_NAME, 35, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
        count_down(WORK_MIN*60)
        reps += 1

def start_button():
    timer_countdown()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_count):
    global timer,reps
    count_min = time_count//60
    count_sec = time_count%60
    if count_min < 10 and count_sec < 10:
        canvas.itemconfig(text_item,text=f"0{count_min}:0{count_sec}")

    elif count_min < 10:
        canvas.itemconfig(text_item,text=f"0{count_min}:{count_sec}")

    elif count_sec < 10:
        canvas.itemconfig(text_item,text=f"{count_min}:0{count_sec}")

    else:
        canvas.itemconfig(text_item,text=f"{count_min}:{count_sec}")

    if time_count > 0:
        timer = window.after(1000,count_down,time_count-1)
    else:
        timer_countdown()
        check_label.config(text=text * (check_count//2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato_image)
text_item = canvas.create_text(103,130,text="25:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)

start_button = Button(text="Start",font=(FONT_NAME,16),highlightthickness=0,command=start_button)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",font=(FONT_NAME,16),highlightthickness=0,command=reset_button)
reset_button.grid(column=2,row=2)

check_label = Label(fg=GREEN,font=(FONT_NAME,16),highlightthickness=0,bg=YELLOW)
check_label.grid(column=1,row=3)

window.mainloop()