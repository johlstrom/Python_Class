from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        label_title.config(text="Break", font=(FONT_NAME, 32), fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", font=(FONT_NAME, 32), fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", font=(FONT_NAME, 32), fg=GREEN, bg=YELLOW)
        count_down(work_sec)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    formatted_min = "{:02d}".format(count_min)
    formatted_sec = "{:02d}".format(count_sec)
    

    canvas.itemconfig(timer_text, text=f"{formatted_min}:{formatted_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "\u2705"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label_title = Label(text="Timer", font=(FONT_NAME, 32), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day28//tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=3)



window.mainloop()