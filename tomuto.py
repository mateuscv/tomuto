import tkinter as tk
import simpleaudio as sa
import win_config as wc
import info

# GLOBAL VARIABLES #

start_minutes = 25  # Change here if you want a different number of minutes
# for the timer
done = False  # Dictates if the timer is done (at 00:00) or not.
sound_flag = True  # Sound on/off toggle flag
on_break = False  # Dictates whether or not the use is on a 10/5 min break
sfx = sa.WaveObject.from_wave_file("resources/boop.wav")  # Boop sfx

# FUNCTION DEFINITIONS #


def prefix_zero(seconds):
    # Adds extra 0 before single-digit seconds

    display_secs = str(seconds)

    if len(display_secs) == 1:
        display_secs = "0" + display_secs

    return display_secs


def timer_display(minutes, seconds, flavor_text):
    global done
    # Updates the timer display every time it's called

    display_secs = prefix_zero(seconds)
    display_mins = prefix_zero(minutes)
    if not done:
        timer_text.config(text=display_mins + ":" + display_secs)
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
    global on_break
    # Does the actual math behind the timer

    if minutes > 0 or seconds > 0:  # If we're not at 00:00, i.e. not done
        if minutes == start_minutes and seconds == 60:  # fresh start
            minutes -= 1
        if seconds > 0:  # Normal seconds countdown during a minute
            seconds -= 1
        else:  # Next minute reached!
            seconds = 59
            minutes -= 1
    else:  # 00:00. Timer done!
        pause_button.configure(state=tk.DISABLED)
        done = True
        on_break = False
        flavor_text.config(text="boop boop!")
        if sound_flag:
            sfx.play()
            root.after(1000, sfx.play)
            root.after(2000, sfx.play)

    return minutes, seconds


def start_caller(minutes, seconds, flavor_text):
    global done
    global five_button
    global ten_button
    global reset_button
    # This calls the start function, but first disables the start button
    # After it has been pressed.

    pause_button.configure(state=tk.NORMAL)
    flavor_text.config(text="running...")
    if on_break:
        flavor_text.config(text="on a break - take your time...")
    start_button.configure(state=tk.DISABLED)
    five_button.configure(state=tk.DISABLED)
    ten_button.configure(state=tk.DISABLED)
    reset_button.configure(state=tk.NORMAL)

    done = False
    start(minutes, seconds, flavor_text)


def reset_buttons_return():
    # Returns the start buttons to clickable after a reset. Must only be available after one second has passed.

    five_button.configure(state=tk.NORMAL)
    ten_button.configure(state=tk.NORMAL)
    start_button.configure(state=tk.NORMAL)


def reset(flavor_text, timer_text):
    global done
    global on_break

    # Activates upon press of the Reset button.

    # Flavor text:

    flavor_text.config(text="tomuto: open source tomato timer")

    # Resetting values:

    done = True
    on_break = False
    minutes = start_minutes
    timer_display_resetter(minutes, timer_text)

    # Configuring start/pause button:

    pause_button.configure(text="Pause")
    pause_button.place(relx=0.35, rely=0.77, anchor="center")
    pause_button.configure(state=tk.DISABLED)

    # Wait before letting start be clickable, so that we don't have two timers at the same time:

    root.after(1000, reset_buttons_return)


def pause_click(flavor_text):
    # Activates on click of the pause button. handles pausing

    minutes, seconds = get_time()  # Now, getting the time that is currently showing...

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

    separator_index = timer_text["text"].index(":")
    minutes = int(timer_text["text"][:separator_index])
    seconds = int(timer_text["text"][separator_index+1:])
    
    return minutes, seconds


def timer_display_resetter(minutes, timer_text):
    # Resets the display to start minutes value when reset is pressed.

    timer_text.config(text=str(minutes) + ":" + "00")


def toggle_sound():
    global sound_flag
    # Toggles sound on or off when the button is pressed

    if sound_flag:
        sound_button.configure(image=no_sound_icon)
        sound_flag = False
    else:
        sound_button.configure(image=sound_icon)
        sound_flag = True


def five_min_break(flavor_text, timer_text):
    global on_break

    flavor_text.config(text="on a break - take your time...")
    timer_text.config(text='05:00')
    five_button.configure(state=tk.DISABLED)
    ten_button.configure(state=tk.DISABLED)
    on_break = True
    start_caller(5, 0, flavor_text)


def ten_min_break(flavor_text, timer_text):
    global on_break

    flavor_text.config(text="on a break - take your time...")
    timer_text.config(text='10:00')
    five_button.configure(state=tk.DISABLED)
    ten_button.configure(state=tk.DISABLED)
    on_break = True
    start_caller(10, 0, flavor_text)


# MAIN #:

root = tk.Tk()  # Starting up the Tkinter window
flavor_text = wc.config_window(root)  # Apply window settings

# Initial timer...:

# ...values:
minutes = start_minutes
seconds = 60

# ...display:

timer_text = tk.Label(text=str(minutes) + ":" + "00") 
timer_text.config(font=("Verdana", 20))
timer_text.pack()

# Configuring the buttons:

sound_icon, no_sound_icon, info_icon, ten_icon, five_icon = wc.get_icons()

start_button = tk.Button(root, text="Start", command=(lambda: start_caller(
    minutes, seconds, flavor_text)))
reset_button = tk.Button(root, text="Reset", command=(lambda: reset(
    flavor_text, timer_text)))
pause_button = tk.Button(root, text="Pause", command=(lambda: pause_click(
    flavor_text)))
sound_button = tk.Button(root, text="", image=sound_icon, command=(
    lambda: toggle_sound()))
info_button = tk.Button(root, text="", image=info_icon, command=(
    lambda: info.open_info_window()))
ten_button = tk.Button(root, text="", image=ten_icon, command=(
    lambda: ten_min_break(flavor_text, timer_text)))
five_button = tk.Button(root, text="", image=five_icon, command=(
    lambda: five_min_break(flavor_text, timer_text)))

#  Placing the buttons:

wc.place_buttons(start_button, reset_button, pause_button, sound_button, info_button, ten_button, five_button)

# The pause button needs to start disabled:

pause_button.configure(state=tk.DISABLED)

root.mainloop()
