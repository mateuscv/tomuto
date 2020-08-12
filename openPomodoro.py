import tkinter as tk
import time

startMinutes = 25 # global variable - change here if you want a different number of minutes for the timer

def configWindow(root):
    # screen resolution and start conditions (gets user's screen width & height; calculate center point; defines title & icon)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    root.geometry("300x100+" + str(int(x)) + "+" + str(int(y)))
    root.title("openPomodoro")
    root.iconbitmap("icon.ico")

    # window text

    text = tk.Label(text="Open Pomodoro Timer")
    text.config(font=("Verdana", 12))
    text.pack()


def prefixZero(seconds):
    # adds extra 0 before single-digit seconds
    displaysecs = str(seconds)

    if len(displaysecs) == 1:
        displaysecs = "0" + displaysecs

    return displaysecs


def timerDisplay(minutes, seconds):
    # updates the timer display every time it's called

    displaysecs = prefixZero(seconds)
    displaymins = prefixZero(minutes)
    timerText.config(text=displaymins + ":" + displaysecs)
    start(minutes, seconds)


def startCaller(minutes, seconds):
    # this calls the start function, but first disables the start button after it has been pressed.
    startButton.configure(state=tk.DISABLED)
    start(minutes, seconds)


def start(minutes, seconds):
    # start the countdown procedure after button press

    done = False
    minutes, seconds, done = countdown(minutes, seconds, done)
    if not done:
        root.after(1000, timerDisplay, minutes, seconds) # calls for an update every second


def countdown(minutes, seconds, done):
    # does the actual math behind the timer

    if (minutes > 0 or seconds > 0): # if we're not on 00:00
        if minutes == startMinutes and seconds == 60: # fresh start
            minutes -= 1
        if seconds > 0: # normal seconds countdown during a minute
            seconds -= 1
        else: # next minute reached!
            seconds = 59
            minutes -= 1
    else:
        startButton.configure(state=tk.ENABLED)
        minutes = startMinutes
        seconds = 60
        done = True

    return minutes, seconds, done


#### MAIN ####:

root = tk.Tk() # starting up the Tkinter window
configWindow(root)

# initial timer...:

#...values:
minutes = startMinutes
seconds = 60

#...display:

timerText = tk.Label(text=str(minutes) + ":" + "00") 
timerText.config(font=("Verdana", 20))
timerText.pack()

# config buttons:

startButton = tk.Button(root, text="Start", command=(lambda:startCaller(minutes, seconds)))
#pauseButton = tk.Button(root, text="Pause", command=(lambda:pause()))               KEY UPCOMING FEATURE
#resetButton = tk.Button(root, text="Reset", command=(lambda:reset()))               KEY UPCOMING FEATURE
startButton.place(relx=0.5, rely=0.77, anchor="center")
#pauseButton.place(relx=0.35, rely=0.77, anchor="center")
#resetButton.place(relx=0.65, rely=0.77, anchor="center")

root.mainloop()