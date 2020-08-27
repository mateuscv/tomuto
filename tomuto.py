import tkinter as tk
import simpleaudio as sa
import info

#### GLOBAL VARIABLES ####

startMinutes = 25 # change here if you want a different number of minutes for the timer
done = False # dictates if the timer is done (at 00:00) or not.
soundFlag = True # sound on/off toggle flag
sfx = sa.WaveObject.from_wave_file("resources/boop.wav") # the boop-boop sound object

#### FUNCTION DEFINITIONS ####

def configWindow(root):
    # screen resolution and start conditions
    # (gets user's screen width & height; calculates center point; defines title & icon)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    root.geometry("300x100+" + str(int(x)) + "+" + str(int(y)))
    root.title("tomuto")
    root.iconbitmap("resources/icon.ico")
    root.resizable(0,0) # remove this line if you want tomuto resizable. Some sizes look funky

    # window text

    flavorText = tk.Label(text="tomuto: open source tomato timer")
    flavorText.config(font=("Verdana", 10))
    flavorText.pack()

    return flavorText

def prefixZero(seconds):
    # adds extra 0 before single-digit seconds

    displaysecs = str(seconds)

    if len(displaysecs) == 1:
        displaysecs = "0" + displaysecs

    return displaysecs


def timerDisplay(minutes, seconds, flavorText):
    global done
    # updates the timer display every time it's called

    displaysecs = prefixZero(seconds)
    displaymins = prefixZero(minutes)
    if not done:
        timerText.config(text=displaymins + ":" + displaysecs)
        start(minutes, seconds, flavorText)


def startCaller(minutes, seconds, flavorText):
    global done
    # this calls the start function, but first disables the start button after it has been pressed.

    pauseButton.configure(state=tk.NORMAL)
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
    global sfx
    # does the actual math behind the timer

    if (minutes > 0 or seconds > 0): # if we're not at 00:00, i.e. not done
        if minutes == startMinutes and seconds == 60: # fresh start
            minutes -= 1
        if seconds > 0: # normal seconds countdown during a minute
            seconds -= 1
        else: # next minute reached!
            seconds = 59
            minutes -= 1
    else: # 00:00. Timer done!
        done = True
        flavorText.config(text="boop boop!")
        if soundFlag:
            sfx.play()

    return minutes, seconds


def reset(flavorText):
    global done
    # activates upon press of the Reset button.

    # flavor text:

    flavorText.config(text="tomuto: open source tomato timer")

    # resetting values:

    done = True
    minutes = startMinutes
    seconds = 60
    timerDisplayResetter(minutes, seconds)

    # configuring start/pause button:

    startButton.configure(state=tk.NORMAL)
    pauseButton.configure(text='Pause')
    pauseButton.place(relx=0.35, rely=0.77, anchor="center")
    pauseButton.configure(state=tk.DISABLED)


def pauseClick(flavorText):
    #what i need to do is get the minutes and seconds it's at, then restart. maybe calling start()

    minutes, seconds = getTime() # now, getting the time that is currently showing...
    paused = pause(flavorText)
    if not paused:
        startCaller(minutes, seconds, flavorText)

def pause(flavorText):
    global done
    # pauses on button press

    if not done:
        flavorText.configure(text="paused")
        done = True
        paused = True
        pauseButton.configure(text='Resume')
        pauseButton.place(relx=0.33, rely=0.77, anchor="center")

    else:
        done = False
        paused = False
        pauseButton.configure(text='Pause')
        pauseButton.place(relx=0.35, rely=0.77, anchor="center")


    return paused


def getTime():
    # gets the currently showing time in integers for both minutes and seconds 

    separatorIndex = timerText['text'].index(":")
    minutes = int(timerText['text'][:separatorIndex])
    seconds = int(timerText['text'][separatorIndex+1:])
    
    return minutes, seconds


def timerDisplayResetter(minutes, seconds):
    # resets the display to start minutes value when reset is pressed.

    timerText.config(text=str(minutes) + ":" + "00")


def toggleSound():
    global soundFlag
    # toggles sound on or off when the button is pressed

    if soundFlag:
        soundButton.configure(image=noSoundIcon)
        soundFlag = False
    else:
        soundButton.configure(image=soundIcon)
        soundFlag = True


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

# configuring the buttons:

soundIcon = tk.PhotoImage(file="resources/sound.png")
noSoundIcon = tk.PhotoImage(file="resources/nosound.png")
infoIcon = tk.PhotoImage(file="resources/info.png")

startButton = tk.Button(root, text="Start", command=(lambda:startCaller(minutes, seconds, flavorText)))
resetButton = tk.Button(root, text="Reset", command=(lambda:reset(flavorText)))
soundButton = tk.Button(root, text="", image=soundIcon, command=(lambda:toggleSound()))
infoButton = tk.Button(root, text="", image=infoIcon, command=(lambda:info.openInfoWindow()))

startButton.place(relx=0.5, rely=0.77, anchor="center")
resetButton.place(relx=0.65, rely=0.77, anchor="center")
soundButton.place(relx=0.96, rely=0.90, anchor="center")
infoButton.place(relx=0.04, rely=0.90, anchor="center")

pauseButton = tk.Button(root, text="Pause", command=(lambda:pauseClick(flavorText)))
pauseButton.configure(state=tk.DISABLED)
pauseButton.place(relx=0.35, rely=0.77, anchor="center")

root.mainloop()
