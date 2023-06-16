from tkinter import *
FONT_NAME = "Courier"


has_writen = True
timer = 0
events = []


def countdown():
    global events
    global has_writen
    global timer
    if timer >= 10:
        has_writen = False
        delete()
        reset()
    global counter
    counter = window.after(1000, countdown)
    global length
    length = len(events)
    timer += 1


def reset():
    window.after_cancel(counter)
    text.insert("1.0", "You exceeded the time limit. For trying again click on start button.")
    reset_timer()


def reset_timer():
    global timer
    timer = 0


def checker(event):
    global has_writen
    global events
    global length
    events.append(event.char)
    if event.char == "":
        has_writen = False
        countdown()
    elif len(events) == length:
        has_writen = False
        countdown()
    if not event.char == "":
        has_writen = True
        reset_timer()


def delete():
    text.delete("1.0", "end -1c")
    text.focus_set()


window = Tk()
window.title('Disappearing Text')
window.wm_attributes('-transparentcolor', '#ab23ff')
canvas = Canvas(height=500, width=1000)
image = PhotoImage(file="background.png")
canvas.create_image(500, 250, image=image)
canvas.grid(row=1, column=1)
text = Text(height=8, width=62, font=(FONT_NAME, 16, "bold"))
text.insert("1.0", "Welcome to Text Disappearing App. If you stop typing, you will have near about 10 seconds to continue "
                   "otherwise all of your efforts will be waste. Click start when you feel ready. Good Luck")
text.place(x=90, y=165)
text.bind("<Key>", checker)
button = Button(text="Start", command=delete, font=("Arial", 10, "normal"), bg="#EA906C")
button.place(x=90, y=365)

window.mainloop()
