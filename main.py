from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_PURPLE = "#3D1766"
PURPLE = "#6F1AB6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=DARK_PURPLE)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        rep = long_break_sec
        title.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        rep = short_break_sec
        title.config(text="Break", fg=PINK)
    else:
        rep = work_sec
        title.config(text="Work", fg=GREEN)

    count_down(rep)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PURPLE)

canvas = Canvas(width=200, height=224, bg=PURPLE, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

title = Label(text="Timer", fg=DARK_PURPLE, font=("Forte", 50, "bold"), bg=PURPLE)
title.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

check_marks = Label(font=("Arial", 20, "bold"), borderwidth=0, bg=PURPLE, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
