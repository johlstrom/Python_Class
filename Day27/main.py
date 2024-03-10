import tkinter

window = tkinter.Tk()
window.title("My first gui")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a label", font=("Comic Sans MS", 24, "bold"))
my_label.pack(side="left")



window.mainloop()