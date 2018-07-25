# Script done by Nekuake using Sivel's speedtest.
import time
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkthemes import ThemedStyle
import os
import speedtest
print("Package found! Ready to run!")
s = speedtest.Speedtest()  # Used

download = 0
upload = 0
ping = 0
timewaited = 0
timessofar = 0
attemps = 0
timesdef = 0
running=0
infinitesting=0

mainwindow = Tk()
mainwindow.tk.call('tk', 'scaling', 2.0)
mainwindow.geometry('800x120')
mainwindow.title("Internet Speed Monitor")
mainwindow.resizable(0,0)
insertstyle = ThemedStyle(mainwindow)
insertstyle.set_theme("black")
mainwindow.configure(bg="#414244")
kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()
deletefile= IntVar()

guiinfinitesting = Checkbutton(mainwindow, text="Infinite", variable=infinitesting, command=lambda:[infcheck()])
guiinfinitesting.grid(row=3,column=4)
guidownloadcheck = Checkbutton(mainwindow, text="Download", variable=kindoftestdown)
guidownloadcheck.grid(row=3, column=0, sticky=NW)
guiuploadcheck = Checkbutton(mainwindow, text="Upload", variable=kindoftestup).grid(row=3, column=1, sticky=NW)
guipingcheck = Checkbutton(mainwindow, text="Ping", variable=kindoftestping).grid(row=3, column=2, sticky=NW)
guiprealloccheck = Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation).grid(row=3, column=3, sticky=SW)
if os.path.isfile("outputgui.txt"):
    guideletefile = Checkbutton(mainwindow,text="Delete old file", variable=deletefile).grid(row=5,column = 1)
Label(mainwindow, text="Nº of tests").grid(row=4, column=0, sticky=NW)

status =Label(mainwindow, text="Waiting for input...")
status.grid(row=6, column=0, sticky=NW,columnspan=5)


times = Spinbox(mainwindow, width=10, from_=1, to=9999, state = 'readonly')
times.grid(row=4, column=1, sticky=NW)
Label(mainwindow, text="Seconds").grid(row=4, column=2, sticky=NW)
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999, state = 'readonly')
timeout.grid(row=4, column=3, sticky=NW)
downloadgui = Label(mainwindow, text="0 MB/s")
downloadgui.grid(row = 3, column = 4, sticky=SE)
mainwindow.grid_columnconfigure(4, pad=4, minsize=200)
pinggui = Label(mainwindow, text="0 ms")
pinggui.grid(row=4, column=4, sticky=SE)
uploadgui = Label(mainwindow, text="0 MB/s")
uploadgui.grid(row=5,column=4, sticky=SE)


def closing():
    if running == 1:
        messagebox.showinfo("Closing Internet Speed Monitor...", "Please, wait until the script closes... It's not frozen. Click OK to start the process of closing")
    exit()

mainwindow.protocol("WM_DELETE_WINDOW", closing)


def infcheck():
    global infinitesting, guiinfinitesting, times
    if infinitesting == 1:
        times.config(state= DISABLED)
    else:
        times.config(state= NORMAL)

globalprogressbar = Progressbar(mainwindow, length=100, mode='determinate', maximum=100)
globalprogressbar.grid(row=6, column = 0,columnspan = 2)
globalprogressbar.place(width=800,height=9)

def test():
    global guirun, mainwindow, testthread, uploadgui, downloadgui, pinggui, timesdef, globalprogressbar, status, running,globalprogressbar
    mainwindow.configure(bg="#f2f4a6")
    print("Starting test function...")
    status.configure(text="Starting test function...")
    running = 1
    timesdef = int(times.get())
    timeoutdef = int(timeout.get())
    timessofar = 1
    timewaited = 0
    kindoftestpingdef = kindoftestping.get()
    kindoftestdowndef = kindoftestdown.get()
    kindoftestupdef = kindoftestup.get()
    portion = (100/(timesdef*(kindoftestupdef+kindoftestdowndef+kindoftestpingdef)))
    if deletefile.get() == 1:
        os.remove("outputgui.txt")
    while timessofar <= timesdef:
            f = open("outputgui.txt", "a")
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
                    status.configure(text="Waiting " + str(timewaited) + " seconds...("+str(timessofar)+"/"+str(timesdef)+")")

            f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
                timessofar) + "/" + str(timesdef) + ": " + str(kindoftestdowndef) + str(kindoftestupdef) + str(kindoftestpingdef) + str(
                timeoutdef) + str(timesdef) + " at time " + time.strftime("%c"))
            if kindoftestdowndef == 1:
                status.configure(text="Testing download speed...("+str(timessofar)+"/"+str(timesdef)+")")
                download = s.download()
                download = download / 1024
                download = round(download)
                f.write("\nDownload Speed (" + str(timessofar) + "): " + str(download) + "KB/s. " + str(
                    download / 1024) + "MB/s")
                downloadgui.configure(text="Download Speed: " + str(download) + " KB/s.")
                globalprogressbar.step(portion)

            if kindoftestpingdef == 1:
                status.configure(text="Testing ping...("+str(timessofar)+"/"+str(timesdef)+")")
                ping = s.lat_lon
                f.write("\nPing:" + str(ping))
                print("\nPing:" + str(ping))
                pinggui.configure(text="Ping: " + str(ping))
                globalprogressbar.step(portion)

            if kindoftestupdef == 1:
                status.configure(text="Testing upload speed...("+str(timessofar)+"/"+str(timesdef)+")")
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
            f.close
            timewaited = timeoutdef

    guirun.configure(state = NORMAL)
    running = 0
    status.configure(text="Finished. Waiting for input... (check outputgui.txt)")
    mainwindow.configure(bg="#F0F0F0")


testthread = [threading.Thread(target=test)]

def init_thread():
    global attemps, testthread
    attemps = attemps + 1
    testthread.insert (attemps,threading.Thread(target=test))
    testthread[attemps].start()




guirun = Button(mainwindow, text="Run", command=lambda: [init_thread(), guirun.configure(state = DISABLED)])
guirun.grid(row=5, column=0, sticky=NW)
mainwindow.mainloop()
