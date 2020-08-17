import tkinter as tk
import time

startMinutes = 25 # global variable - change here if you want a different number of minutes for the timer
done = False # dictates if the timer is done or not.

def configWindow(root):
    # screen resolution and start conditions
    # (gets user's screen width & height; calculates center point; defines title & icon)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    root.geometry("300x100+" + str(int(x)) + "+" + str(int(y)))
    root.title("tomuto")
    root.iconbitmap("icon.ico")

    # window text

    flavorText = tk.Label(text="tomuto: open source pomodoro")
    flavorText.config(font=("Verdana", 12))
    flavorText.pack()

    return flavorText

def prefixZero(seconds):
    # adds extra 0 before single-digit seconds
    displaysecs = str(seconds)

    if len(displaysecs) == 1:
        displaysecs = "0" + displaysecs

    return displaysecs

def timerDisplay(minutes, seconds, flavorText):
    # updates the timer display every time it's called
    displaysecs = prefixZero(seconds)
    displaymins = prefixZero(minutes)
    timerText.config(text=displaymins + ":" + displaysecs)
    if not done:
        start(minutes, seconds, flavorText)


def startCaller(minutes, seconds, flavorText):
    global done
    # this calls the start function, but first disables the start button after it has been pressed.

    flavorText.config(text='running...')
    startButton.configure(state=tk.DISABLED)
    resetButton.configure(state=tk.NORMAL)

    done = False
    start(minutes, seconds, flavorText)


def start(minutes, seconds, flavorText):
    global done
    # start the countdown procedure after button press

    minutes, seconds = countdown(minutes, seconds, flavorText)
    if not done:
        root.after(1000, timerDisplay, minutes, seconds, flavorText) # calls for an update every second


def countdown(minutes, seconds, flavorText):
    global done
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
        done = True
        flavorText.config(text="boop boop!")

    return minutes, seconds


def reset(flavorText):
    global done
    # activates upon press of the Reset button.

    # flavor text:

    flavorText.config(text="tomuto: open source pomodoro")

    # resetting values:

    done = True
    minutes = startMinutes
    seconds = 60
    timerDisplayResetter(minutes, seconds)

    # re-enabling start button:

    startButton.configure(state=tk.NORMAL)


def timerDisplayResetter(minutes, seconds):
    # resets the display to start minutes value when reset is pressed.

    timerText.config(text=str(minutes) + ":" + "00")


#### MAIN ####:

root = tk.Tk() # starting up the Tkinter window
flavorText = configWindow(root) # apply window settings

# initial timer...:

#...values:
minutes = startMinutes
seconds = 60

#...display:

timerText = tk.Label(text=str(minutes) + ":" + "00") 
timerText.config(font=("Verdana", 20))
timerText.pack()

# config buttons:

startButton = tk.Button(root, text="Start", command=(lambda:startCaller(minutes, seconds, flavorText)))
#pauseButton = tk.Button(root, text="Pause", command=(lambda:pause()))               KEY UPCOMING FEATURE
resetButton = tk.Button(root, text="Reset", command=(lambda:reset(flavorText)))               #KEY WIP FEATURE
resetButton.configure(state=tk.DISABLED)
startButton.place(relx=0.5, rely=0.77, anchor="center")
#pauseButton.place(relx=0.35, rely=0.77, anchor="center")
resetButton.place(relx=0.65, rely=0.77, anchor="center")

root.mainloop()