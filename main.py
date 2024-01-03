import tkinter
import time
import datetime
from threading import Timer
import tkinter.messagebox


LASTKEYPRESS = 0

def get_text():
    global LASTKEYPRESS
    stilltyping = True
    while stilltyping:
        if LASTKEYPRESS < datetime.datetime.now().timestamp() - 5:
            typing_box.delete("1.0", tkinter.END)


def start_deleting():
    Timer(5, get_text).start()



window = tkinter.Tk()
window.title(
    "Typer of Doom"
)
title = tkinter.Label(
    text = "Keep typing or your work get deleted!!!!"
)

title.pack(
    anchor='center'
)
typing_box = tkinter.Text(
    height=20,
    width=52
)
typing_box.pack(
    anchor='center'
)
start_button = tkinter.Button(
    text='Start',
    command=start_deleting
)
start_button.pack(
    anchor='center',
    ipadx=10,
    ipady=10,

)

def key_press(e):
    global LASTKEYPRESS
    LASTKEYPRESS = datetime.datetime.now().timestamp()


window.bind('<KeyPress>',key_press)


window.mainloop()