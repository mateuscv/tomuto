import tkinter as tk
import simpleaudio as sa
import win_config as wc
import info

#### GLOBAL VARIABLES ####

start_minutes = 25 # Change here if you want a different number of minutes 
# for the timer
done = False # Dictates if the timer is done (at 00:00) or not.
sound_flag = True # Sound on/off toggle flag
sfx = sa.WaveObject.from_wave_file("resources/boop.wav") # Boop sfx

#### FUNCTION DEFINITIONS ####


def prefix_zero(seconds):
    # Adds extra 0 before single-digit seconds

    displaysecs = str(seconds)

    if len(displaysecs) == 1:
        displaysecs = "0" + displaysecs

    return displaysecs


def timer_display(minutes, seconds, flavor_text):
    global done
    # Updates the timer display every time it's called

    displaysecs = prefix_zero(seconds)
    displaymins = prefix_zero(minutes)
    if not done:
        timer_text.config(text=displaymins + ":" + displaysecs)
        start(minutes, seconds, flavor_text)


def start(minutes, seconds, flavor_text):
    global done
    # Start the countdown procedure after button press

    minutes, seconds = countdown(minutes, seconds, flavor_text)
    if not done:
        root.after(1000, timer_display, minutes, seconds, flavor_text) 
        # ^ Calls for an update every second


def countdown(minutes, seconds, flavor_text):
    global done
    global sfx
    # Does the actual math behind the timer

    if (minutes > 0 or seconds > 0): # If we're not at 00:00, i.e. not done
        if minutes == start_minutes and seconds == 60: # fresh start
            minutes -= 1
        if seconds > 0:  # Normal seconds countdown during a minute
            seconds -= 1
        else:  # Next minute reached!
            seconds = 59
            minutes -= 1
    else:  # 00:00. Timer done!
        done = True
        flavor_text.config(text="boop boop!")
        if sound_flag:
            sfx.play()

    return minutes, seconds


def start_caller(minutes, seconds, flavor_text):
    global done
    # This calls the start function, but first disables the start button
    # After it has been pressed.

    pause_button.configure(state=tk.NORMAL)
    flavor_text.config(text="running...")
    start_button.configure(state=tk.DISABLED)
    reset_button.configure(state=tk.NORMAL)

    done = False
    start(minutes, seconds, flavor_text)


def reset(flavor_text):
    global done
    # Activates upon press of the Reset button.

    # Flavor text:

    flavor_text.config(text="tomuto: open source tomato timer")

    # Resetting values:

    done = True
    minutes = start_minutes
    seconds = 60
    timer_displayResetter(minutes, seconds)

    # Configuring start/pause button:

    start_button.configure(state=tk.NORMAL)
    pause_button.configure(text="Pause")
    pause_button.place(relx=0.35, rely=0.77, anchor="center")
    pause_button.configure(state=tk.DISABLED)


def pause_click(flavor_text):
    # Activates on click of the pause button. handles pausing

    minutes, seconds = get_time()  # Now, getting the time that is currently 
    #showing...
    paused = pause(flavor_text)
    if not paused:
        start_caller(minutes, seconds, flavor_text)


def pause(flavor_text):
    global done
    # Pauses on button press

    if not done:
        flavor_text.configure(text="paused")
        done = True
        paused = True
        pause_button.configure(text="Resume")
        pause_button.place(relx=0.33, rely=0.77, anchor="center")

    else:
        done = False
        paused = False
        pause_button.configure(text="Pause")
        pause_button.place(relx=0.35, rely=0.77, anchor="center")

    return paused


def get_time():
    # Gets the currently showing time in integers for both minutes and 
    # seconds 

    separatorIndex = timer_text["text"].index(":")
    minutes = int(timer_text["text"][:separatorIndex])
    seconds = int(timer_text["text"][separatorIndex+1:])
    
    return minutes, seconds


def timer_displayResetter(minutes, seconds):
    # Resets the display to start minutes value when reset is pressed.

    timer_text.config(text=str(minutes) + ":" + "00")


def toggleSound():
    global sound_flag
    # Toggles sound on or off when the button is pressed

    if sound_flag:
        sound_button.configure(image=no_sound_icon)
        sound_flag = False
    else:
        sound_button.configure(image=sound_icon)
        sound_flag = True


#### MAIN ####:

root = tk.Tk()  # Starting up the Tkinter window
flavor_text = wc.config_window(root)  # Apply window settings

# Initial timer...:

#...values:
minutes = start_minutes
seconds = 60

#...display:

timer_text = tk.Label(text=str(minutes) + ":" + "00") 
timer_text.config(font=("Verdana", 20))
timer_text.pack()

# Configuring the buttons:

sound_icon, no_sound_icon, info_icon = wc.get_icons() #  Get the icons

start_button = tk.Button(root, text="Start", command=(lambda:start_caller(
    minutes, seconds, flavor_text)))
reset_button = tk.Button(root, text="Reset", command=(lambda:reset(
    flavor_text)))
pause_button = tk.Button(root, text="Pause", command=(lambda:pause_click(
    flavor_text)))
sound_button = tk.Button(root, text="", image=sound_icon, command=(
    lambda:toggleSound()))
info_button = tk.Button(root, text="", image=info_icon, command=(
    lambda:info.open_info_window()))

wc.place_buttons(start_button, reset_button, pause_button, sound_button,
 info_button) #  Place the buttons

pause_button.configure(state=tk.DISABLED)

root.mainloop()
