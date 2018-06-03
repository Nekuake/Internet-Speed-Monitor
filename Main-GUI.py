# Script done by Nekuake using Sivel's speedtest.
import time
import os
import tkinter as tk
from tkinter import *
mainwindow = Tk ()
mainwindow.geometry ('400x500')
mainwindow.configure(bg = "white")
mainwindow.title("Internet Speed Monitor")
download = "0"
upload = "0"
ping = "0"
downloadgui = tk.Message(mainwindow, text=download)
uploadgui = tk.Message(mainwindow, text=upload)
pingui = tk.Message(mainwindow, text=upload)
downloadgui.config(font=('sans', 24))
downloadgui.pack()
uploadgui.config(font=('sans', 24))
uploadgui.pack()
pingui.config(font=('sans', 24))
pingui.pack()
print("Please, be sure that you have it first.\n")
try:
    import speedtest
    print("Package found! Ready to run!")
    s = speedtest.Speedtest()  # Used
    speedtestfound=1
except ImportError as e:  # Package not found, scipt shouldn't be run
    speedtestfound = 0
mainwindow.mainloop()