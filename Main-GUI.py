# Script done by Nekuake using Sivel's speedtest.
import time
import threading
import errno
import json
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import speedtest
import math
#Keys:
print("Package found! Ready to run!")
s = speedtest.Speedtest()  # Used
print("Creating variables...")
download = 0
upload = 0
ping = 0
timewaited = 0
timessofar = 0
attemps = 0
timesdef = 0
running = 0
try:
    os.makedirs("Logs")
    print("Folder created!!")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
print("Creating the window...")
mainwindow = Tk()
try:
    from ttkthemes import ThemedStyle

    insertstyle = ThemedStyle(mainwindow)
    insertstyle.set_theme("black")
    mainwindow.configure(bg="#414244")
except:
    messagebox.showinfo("TTK ERROR",
                        "TTKthemes not installed. Run python -m pip install ttkthemes. Using default theme")
mainwindow.tk.call('tk', 'scaling', 1.7)
mainwindow.geometry('800x220')
mainwindow.title("Internet Speed Monitor")
mainwindow.resizable(0, 0)
try:
    mainwindow.iconbitmap('internet.ico')
except:
    print("WARNING: ICON NOT FOUND (executable?)")

print("Creating more variables...")
kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()
deletefile = IntVar()
infinitesting = IntVar()
print("Creating the windgets...")
guiinfinitesting = Checkbutton(mainwindow, text="Infinite", variable=infinitesting)
guiinfinitesting.grid(row=3, column=4, sticky=W)
guidownloadcheck = Checkbutton(mainwindow, text="Download", variable=kindoftestdown)
guidownloadcheck.grid(row=3, column=0, sticky=NW)
guiuploadcheck = Checkbutton(mainwindow, text="Upload", variable=kindoftestup).grid(row=3, column=1, sticky=NW)
guipingcheck = Checkbutton(mainwindow, text="Ping", variable=kindoftestping).grid(row=3, column=2, sticky=NW)
guiprealloccheck = Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation).grid(row=3,
                                                                                                                  column=3,
                                                                                                                  sticky=SW)
CountryNameTkinter=Label(mainwindow, text="Country:")
CountryNameTkinter.grid(row=7, column=0)
Label(mainwindow, text="Nº of tests").grid(row=4, column=0, sticky=NW)

status = Label(mainwindow, text="Waiting for input...")
status.grid(row=6, column=0, sticky=NW, columnspan=5)

times = Spinbox(mainwindow, width=10, from_=1, to=9999, state='readonly')
times.grid(row=4, column=1, sticky=NW)
Label(mainwindow, text="Seconds").grid(row=4, column=2, sticky=NW)
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999, state='readonly')
timeout.grid(row=4, column=3, sticky=NW)
downloadgui = Label(mainwindow, text="0 MB/s")
downloadgui.grid(row=3, column=4, sticky=SE)
mainwindow.grid_columnconfigure(4, pad=4, minsize=200)
pinggui = Label(mainwindow, text="0 ms")
pinggui.grid(row=4, column=4, sticky=SE)
uploadgui = Label(mainwindow, text="0 MB/s")
uploadgui.grid(row=5, column=4, sticky=SE)
authorgui = Label(mainwindow, text="By Nekuake")
authorgui.grid(row=6, column=4, sticky=SE)


def closing():
    if running == 1:
        messagebox.showinfo("Closing Internet Speed Monitor...",
                            "Please, wait until the script closes... It's not frozen. Click OK to start the process of closing. If it doesn't work, close the console window...")
    exit()


mainwindow.protocol("WM_DELETE_WINDOW", closing)

globalprogressbar = Progressbar(mainwindow, length=100, mode='determinate', maximum=100)
globalprogressbar.grid(row=6, column=0, columnspan=2)
globalprogressbar.place(width=800, height=9, y=111)


def test():
    global guirun, mainwindow, testthread, uploadgui, downloadgui, pinggui, timesdef, globalprogressbar, status, running, globalprogressbar, infinitesting
    print("Starting test function...")
    status.configure(text="Starting test function...")
    print(infinitesting)
    infinitestingdef = infinitesting.get()
    print(infinitestingdef)
    running = 1
    timesdef = int(times.get())
    timeoutdef = int(timeout.get())
    if infinitestingdef == 1:
        timesdef = math.inf
    timessofar = 1
    timewaited = 0
    kindoftestpingdef = kindoftestping.get()
    kindoftestdowndef = kindoftestdown.get()
    kindoftestupdef = kindoftestup.get()
    try:
        portion = (100 / (timesdef * (kindoftestupdef + kindoftestdowndef + kindoftestpingdef)))
    except ZeroDivisionError:
        running = 0
        guirun.configure(state=NORMAL)
        messagebox.showerror("No tests selected", "At least one kind of test must be selected.")
        status.configure(text="INPUT ERROR. Select one kind of test")
        return
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "Logs/GUI_TEST_" + time.strftime("%Y-%m-%d_%H-%M-%S") + "_GUI.txt")

    while timessofar <= timesdef:
        f = open(filename, "a")
        if timessofar == 1:
            print("Getting best server...")
            status.configure(text="Getting best server...")
            s.get_best_server()
            print("Best server acquired!")
            print(
                "\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(timesdef) + str(
                    kindoftestupdef) + str(
                    kindoftestdowndef) + str(kindoftestpingdef) + str(timeoutdef))
            f.write("\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(timesdef) + str(
                kindoftestupdef) + str(
                kindoftestdowndef) + str(kindoftestpingdef) + str(timeoutdef))
        else:
            print("Waiting", str(timeoutdef), " seconds...")
            while timewaited != 0:
                time.sleep(1)
                timewaited = timewaited - 1
                status.configure(
                    text="Waiting " + str(timewaited) + " seconds...(" + str(timessofar) + "/" + str(timesdef) + ")")

        f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
            timessofar) + "/" + str(timesdef) + ": " + str(kindoftestdowndef) + str(kindoftestupdef) + str(
            kindoftestpingdef) + str(
            timeoutdef) + str(timesdef) + " at time " + time.strftime("%c"))
        if kindoftestdowndef == 1:
            status.configure(text="Testing download speed...(" + str(timessofar) + "/" + str(timesdef) + ")")
            download = s.download()
            download = download / 1024
            download = round(download)
            f.write("\nDownload Speed (" + str(timessofar) + "): " + str(download) + "KB/s. " + str(
                download / 1024) + "MB/s")
            downloadgui.configure(text="Download Speed: " + str(download) + " KB/s.")
            globalprogressbar.step(portion)

        if kindoftestpingdef == 1:
            status.configure(text="Testing ping...(" + str(timessofar) + "/" + str(timesdef) + ")")
            ping = s.lat_lon
            f.write("\nPing:" + str(ping))
            print("\nPing:" + str(ping))
            pinggui.configure(text="Ping: " + str(ping))
            globalprogressbar.step(portion)

        if kindoftestupdef == 1:
            status.configure(text="Testing upload speed...(" + str(timessofar) + "/" + str(timesdef) + ")")
            if memorypreallocation == "Y":
                upload = s.upload(pre_allocate=False)
            elif memorypreallocation != "Y":
                upload = s.upload()
            upload = upload / 1024
            upload = round(upload)
            print("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
            f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
            uploadgui.configure(text="Upload Speed: " + str(upload) + " KB/s.")
            globalprogressbar.step(portion)

        timessofar = timessofar + 1
        f.close()
        timewaited = timeoutdef

    guirun.configure(state=NORMAL)
    running = 0
    status.configure(text="Finished. Waiting for input... (check" + filename + ")")


testthread = [threading.Thread(target=test)]


def init_thread():
    global attemps, testthread
    attemps = attemps + 1
    testthread.insert(attemps, threading.Thread(target=test))
    testthread[attemps].start()


guirun = Button(mainwindow, text="Run", command=lambda: [init_thread(), guirun.configure(state=DISABLED)])
guirun.grid(row=5, column=0, sticky=NW)
mainwindow.mainloop()
