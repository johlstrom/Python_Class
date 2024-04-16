from tkinter import *

def button_clicked():
    text_input = input.get()
    km = round(int(text_input) * 1.61, 1)
    answer_label.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)


km = 0

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

#Labels
miles_label = Label(text="Miles", font=("Comic Sans MS", 14, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Comic Sans MS", 14, "bold"))
equal_label.grid(column=0, row=1)

answer_label = Label(text=km, font=("Comic Sans MS", 14, "bold"))
answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Comic Sans MS", 14, "bold"))
km_label.grid(column=2, row=1)

#Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)








window.mainloop()
