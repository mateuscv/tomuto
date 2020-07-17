import datetime
import time
import tkinter as tk

def configWindow(window, timer):

    # screen resolution and start conditions (gets user's screen width & height; calculate center point; defines title & icon)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    window.geometry("300x100+" + str(int(x)) + "+" + str(int(y)))
    window.title("openPomodoro")
    window.iconbitmap("icon.ico")

    # window text, including default timer

    text = tk.Label(text="Open Pomodoro Timer")
    text.config(font=("Verdana", 12))
    timerText = tk.Label(text=str(timer.time())[3:])
    timerText.config(font=("Verdana", 20))
    text.pack()
    timerText.pack()

    # window buttons

    startButton = tk.Button(window, text="Start", command=(lambda:start(timer, timerText, window)))
    pauseButton = tk.Button(window, text="Pause", command=(lambda:pause()))
    resetButton = tk.Button(window, text="Reset", command=(lambda:reset()))
    startButton.place(relx=0.35, rely=0.77, anchor="center")
    pauseButton.place(relx=0.5, rely=0.77, anchor="center")
    resetButton.place(relx=0.65, rely=0.77, anchor="center")

    return 0

def pause(timer):
    return 0
def reset(timer):
    timer = datetime.time(minute=25,second=0)
    return timer

def start(timer, timerText, window):
    countdown(timer, timerText, window)
    return 0

def countdown(timer, timerText, window):
    td = datetime.timedelta(seconds=1)
    timer -= td
    window.after(1000, timerText.config(text=str(timer.time())[3:]))

timer = datetime.datetime(100,1,1,11,25,0)
window = tk.Tk()
configWindow(window, timer)
window.mainloop()