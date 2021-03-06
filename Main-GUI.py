# Script done by Nekuake using Sivel's speedtest.

from tkinter import *

booted= 0
loadingwindow=Tk()
loadingwindow.geometry("100x40")
loadingwindow.title("Loading Internet Speed Monitor")
guiloadingwindowlabel=Label(loadingwindow, text="Loading program...")
guiloadingwindowlabel.place(x=0, y=0)
loadingwindow.update()
print("Booting...")

import time
import errno
import platform
import threading
from tkinter.ttk import *
from tkinter import messagebox
import os
import speedtest
import math
import glob
from tkinter import ttk
systemrunning=platform.system()
print (systemrunning)
if systemrunning == "Windows":
    import winsound
# Keys: name, sponsor, country, url

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
kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()
deletefile = IntVar()
infinitesting = IntVar()
s = ttk.Style()
s.theme_names()
s.theme_use('vista')
#Style



mainwindow.tk.call('tk', 'scaling', 2)
mainwindow.geometry('400x500')
mainwindow.title("Internet Speed Monitor by Nekuake running in " + os.path.dirname(__file__))
mainwindow.resizable(0, 0)
try:
    mainwindow.iconbitmap('internet.ico')
except:
    print("WARNING: ICON NOT FOUND (executable?)")


print("Creating the widgets...")

guidownloadcheck = Checkbutton(mainwindow, text="Download", variable=kindoftestdown)
guiuploadcheck = Checkbutton(mainwindow, text="Upload", variable=kindoftestup)
guipingcheck = Checkbutton(mainwindow, text="Ping", variable=kindoftestping)
guiprealloccheck = Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation)
guinumberoftests = Label(mainwindow, text="Nº of tests")
status = Label(mainwindow, text="Waiting for input...")
times = Spinbox(mainwindow, width=10, from_=1, to=9999, state='readonly')
guitextseconds=Label(mainwindow, text="Seconds")
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999, state='readonly')
downloadgui = Label(mainwindow, text="0 MB/s")
pinggui = Label(mainwindow, text="0 ms")
uploadgui = Label(mainwindow, text="0 MB/s")
authorgui = Label(mainwindow, text="By Nekuake")
globalprogressbar = Progressbar(mainwindow, length=100, mode='determinate', maximum=100)
waitprogressbar = Progressbar(mainwindow, length=100, mode='determinate', maximum=100)
guiservercountry=Label(mainwindow, text="Country")
guiserversponsor=Label(mainwindow, text="Sponsor")
guiservername=Label(mainwindow, text="Name")

guidownloadcheck.place(x=10, y=5)
guiuploadcheck.place(x=10, y=60)
guinumberoftests.place(x=150,y=5)
guipingcheck.place(x=10, y=180)
guiprealloccheck.place(x=10, y=120)
status.place(x=5, y=230)
times.place(x=270, y=5)
guitextseconds.place(x=168,y=60)
timeout.place(x=270,y=60)
downloadgui.place(x=400, y=300, anchor=NE)
pinggui.place(x=400,y=430, anchor=NE)
uploadgui.place(x=400,y=360, anchor=NE)
authorgui.place(x=140, y= 470)
globalprogressbar.place(width=400, height=10, y=220)
waitprogressbar.place(width=400, height=10, y=260)
guiservername.place(x=10, y=270)
guiservercountry.place(x=10, y=330)
guiserversponsor.place(x=10, y=400)

def closing():
    if running == 1:
        messagebox.showinfo("Closing Internet Speed Monitor...",
                            "Please, wait until the script closes... It's not frozen. Click OK to start the process of closing. If it doesn't work, close the console window...")
    sys.exit(0)


mainwindow.protocol("WM_DELETE_WINDOW", closing)






def test():
    global guirun, mainwindow, testthread, uploadgui, downloadgui, pinggui, timesdef, globalprogressbar, status, running,\
        globalprogressbar, infinitesting, waitprogressbar, systemrunning, testfilename, guiserversponsor,\
        guiservercountry, guiservername, guidownloadcheck, guiuploadcheck, guinumberoftests, guipingcheck, guiprealloccheck,\
        guiinfinitesting, guitextseconds, timeout, times
    guidownloadcheck.configure(state=DISABLED)
    guiuploadcheck.configure(state=DISABLED)
    guinumberoftests.configure(state=DISABLED)
    guipingcheck.configure(state=DISABLED)
    guiprealloccheck.configure(state=DISABLED)
    guiinfinitesting.configure(state=DISABLED)
    guitextseconds.configure(state=DISABLED)
    timeout.configure(state=DISABLED)
    times.configure(state=DISABLED)
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
    waitportion=(100/timeoutdef)
    try:
        portion = (100 / (timesdef * (kindoftestupdef + kindoftestdowndef + kindoftestpingdef)))
    except ZeroDivisionError:
        running = 0
        guirun.configure(state=NORMAL)
        if systemrunning == "Windows":
            print("Error on Windows. Playing sound.")
            winsound.PlaySound("SystemHand",winsound.SND_ASYNC)
        status.configure(text="INPUT ERROR. Select one kind of test")
        return
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "Logs/GUI_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt")

    while timessofar <= timesdef:
        f = open(filename, "a")
        if timessofar == 1:
            print("Getting best server...")
            status.configure(text="Getting best server...")
            serverdata=s.get_best_server()
            servercountry=serverdata["country"]
            serversponsor=serverdata["sponsor"]
            servername=serverdata["name"]
            serverurl=serverdata["url"]
            guiservername.configure(text=servername)
            guiservercountry.configure(text=servercountry)
            guiserversponsor.configure(text=serversponsor)
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
                waitprogressbar.step(waitportion)
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
    guidownloadcheck.configure(state=NORMAL)
    guiuploadcheck.configure(state=NORMAL)
    guinumberoftests.configure(state=NORMAL)
    guipingcheck.configure(state=NORMAL)
    guiprealloccheck.configure(state=NORMAL)
    guiinfinitesting.configure(state=NORMAL)
    guitextseconds.configure(state=NORMAL)
    timeout.configure(state="readonly")
    guirun.configure(state=NORMAL)
    times.configure(state="readonly")
    running = 0
    status.configure(text="Finished. Waiting for input...")


testthread = [threading.Thread(target=test)]


def init_thread():
    global attemps, testthread
    attemps = attemps + 1
    testthread.insert(attemps, threading.Thread(target=test))
    testthread[attemps].start()


def disable_spinbox():
    global infinitesting, guinumberoftests, times
    infinitcheck=infinitesting.get()
    if infinitcheck == 1:
        guinumberoftests.configure(state=DISABLED)
        times.configure(state=DISABLED)
        print("STATE=DISABLED")
    else:
        guinumberoftests.configure(state=NORMAL)
        times.configure(state="readonly")
        print("STATE=ENABLED")

def log_explorer():
    files = (glob.glob(os.path.dirname(__file__) + "/Logs/*.txt"))
    for x in files:
        print(x)



logexplorerwindow = threading.Thread(target=log_explorer)
logexplorerwindow.start()

guirun = Button(mainwindow, text="Run", command=lambda: [init_thread(), guirun.configure(state=DISABLED)])
guiinfinitesting = Checkbutton(mainwindow, text="Infinite", variable=infinitesting,  command= disable_spinbox)
guirun.place(x=208 , y=180, width = 180)
guiinfinitesting.place(x=110, y=180)

print("Displaying window...")
loadingwindow.withdraw()
mainwindow.deiconify()
mainwindow.mainloop()
