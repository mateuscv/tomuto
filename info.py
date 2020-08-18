import tkinter as tk
import webbrowser

def openInfoWindow():
    # makes and shows info window on button press.

    tomutoInfo = tk.Toplevel()
    tomutoInfo.title("tomuto - info")
    tomutoInfo.iconbitmap("resources/icon.ico")

    # geometry info
    screen_width = tomutoInfo.winfo_screenwidth()
    screen_height = tomutoInfo.winfo_screenheight()
    x = (screen_width/2) - (300/2)
    y = (screen_height/2) - (100/2)
    tomutoInfo.geometry("275x150+" + str(int(x-50)) + "+" + str(int(y)-40))
    tomutoInfo.resizable(0,0)

    tomutoName = tk.Label(tomutoInfo, text="tomuto")
    tomutoName.config(font=("Verdana", 20), fg='red')
    tomutoName.pack()

    description = tk.Label(tomutoInfo, text='open source pomodoro timer')
    description.pack(pady=(0,10))

    github = tk.Label(tomutoInfo, text="More info and source code:")
    github.pack()
    link = tk.Label(tomutoInfo, text="tomuto on Github", fg='blue', cursor='hand2')
    link.pack()
    link.bind("<Button-1>", lambda l: callback("https://github.com/mateuscv/tomuto"))

    originalDeveloper = tk.Label(tomutoInfo, text="Created with ♥ by Mateus Cappellari Vieira")
    originalDeveloper.pack(pady=(10,0))

def callback(url):
    # opens the github link
    webbrowser.open_new(url)
