import tkinter as tk


def config_window(root):
    # Screen resolution and start conditions
    # (gets user's screen width & height; center point; title & icon)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    root.geometry("300x100+" + str(int(x)) + "+" + str(int(y)))
    root.title("tomuto")
    root.iconbitmap("resources/icon.ico")
    root.resizable(0, 0)  # Remove this if you want tomuto resizable.

    # Window text

    flavor_text = tk.Label(text="tomuto: open source tomato timer")
    flavor_text.config(font=("Verdana", 10))
    flavor_text.pack()

    return flavor_text


def get_icons():
    # Imports the icons from files and returns them

    sound_icon = tk.PhotoImage(file="resources/sound.png")
    no_sound_icon = tk.PhotoImage(file="resources/nosound.png")
    info_icon = tk.PhotoImage(file="resources/info.png")
    tenicon = tk.PhotoImage(file="resources/10minbreak.png")
    fiveicon = tk.PhotoImage(file="resources/5minbreak.png")

    return sound_icon, no_sound_icon, info_icon, tenicon, fiveicon


def place_buttons(start_button, reset_button, pause_button, sound_button,
                  info_button, ten_button, five_button):
    # Initial button placements

    start_button.place(relx=0.5, rely=0.77, anchor="center")
    reset_button.place(relx=0.65, rely=0.77, anchor="center")
    pause_button.place(relx=0.35, rely=0.77, anchor="center")
    sound_button.place(relx=0.96, rely=0.90, anchor="center")
    info_button.place(relx=0.04, rely=0.90, anchor="center")
    ten_button.place(relx=0.11, rely=0.90, anchor="center")
    five_button.place(relx=0.89, rely=0.90, anchor="center")
