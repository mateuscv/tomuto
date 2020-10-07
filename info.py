import tkinter as tk
import webbrowser


def open_info_window():
    # Makes and shows info window on button press.

    tomuto_info = tk.Toplevel()
    tomuto_info.title("tomuto - info")
    tomuto_info.iconbitmap("resources/icon.ico")

    # Geometry info
    screen_width = tomuto_info.winfo_screenwidth()
    screen_height = tomuto_info.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    tomuto_info.geometry("270x165+" + str(int(x-50)) + "+" + str(int(y)-40))
    tomuto_info.resizable(0, 0)

    # Widgets

    tomuto_name = tk.Label(tomuto_info, text="tomuto")
    tomuto_name.config(font=("Verdana", 20), fg='red')
    tomuto_name.pack()

    description = tk.Label(tomuto_info, text='open source tomato timer')
    description.pack(pady=(0, 10))

    github = tk.Label(tomuto_info, text="More info and source code:")
    github.pack()
    link = tk.Label(tomuto_info, text="tomuto on Github", fg='blue', cursor='hand2')
    link.pack()
    link.bind("<Button-1>", lambda l: callback("https://github.com/mateuscv/tomuto"))

    original_developer = tk.Label(tomuto_info, text="Created with ♥ by Mateus Cappellari Vieira")
    original_developer.pack(pady=(10, 0))

    version = tk.Label(tomuto_info, text='development build 0.9.1')
    version.pack(pady=(1, 0))
    version.config(font=("Verdana", 8), fg='gray')


def callback(url):
    # Opens the github link

    webbrowser.open_new(url)
