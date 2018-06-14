# Script done by Nekuake using Sivel's speedtest.
import time
import os
import tkinter as tk
from tkinter import *

try:
    import speedtest

    print("Package found! Ready to run!")
    s = speedtest.Speedtest()  # Used
    status = 0
except ImportError as e:  # Package not found, scipt shouldn't be run
    status = -1
mainwindow = Tk()
mainwindow.tk.call('tk', 'scaling', 2.0)
mainwindow.geometry('500x300')
mainwindow.configure(bg="#F0F0F0")
mainwindow.title("Internet Speed Monitor")
download = "0"
upload = "0"
ping = "0"
times = 0
kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()

Checkbutton(mainwindow, text="Download", variable=kindoftestdown).grid(row=3, column=0, sticky=NW)
Checkbutton(mainwindow, text="Upload", variable=kindoftestup).grid(row=3, column=1, sticky=NW)
Checkbutton(mainwindow, text="Ping", variable=kindoftestping).grid(row=3, column=2, sticky=NW)
Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation).grid(row=3, column=3,
                                                                                               sticky=SW)
Label(mainwindow, text="Nº of tests").grid(row=4, column=0, sticky=NW)
times = Spinbox(mainwindow, width=10, from_=1, to=9999)
times.grid(row=4, column=1, sticky=NW)
Label(mainwindow, text="Seconds").grid(row=4, column=2, sticky=NW)
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999)
timeout.grid(row=4, column=3, sticky=NW)
Label(mainwindow, textvariable=download).grid(row=1, column=0, sticky=NW)
Label(mainwindow, textvariable=upload).grid(row=1, column=1, sticky=NW)
Label(mainwindow, textvariable=ping).grid(row=1, column=2, sticky=NW)
if status == 0:
    Label(mainwindow, text="OK. Waiting conf.", fg="green").grid(row=5, column=0)
elif status == -1:
    Label(mainwindow, text="INSTALL THE SPEEDTEST PYTHON MODULE", fg="red").grid(row=5, column=0, sticky=NW)
elif status == 5:
    Label(mainwindow, text="Waiting" + timeout + "seconds", fg="purple").grid(row=5, column=0, sticky=NW)
elif status == 1:
    Label(mainwindow, text="INSTALL THE SPEEDTEST PYTHON MODULE", fg="red").grid(row=5, column=0, sticky=NW)


def test():
    global times, download, upload, ping, kindoftestping, kindoftestdown, kindoftestdown, kindoftestping, timeout, status
    timesdef = int(times.get())
    timeoutdef = int(timeout.get())
    timessofar = 1
    status = 1
    while timessofar <= timesdef:
        f = open("outputgui.txt", "a")
        if timessofar == 1:
            print(
                "\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(timesdef) + str(kindoftestup) + str(
                    kindoftestdown) + str(kindoftestping) + str(timeoutdef))
            f.write("\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(times) + str(kindoftestup) + str(
                kindoftestdown) + str(kindoftestping) + str(timeout))
        else:
            print("Waiting", timeout, " seconds...")
            status = 5
            time.sleep(timeoutdef)
        f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
            timessofar) + "/" + str(times) + ": " + str(kindoftestdown) + str(kindoftestup) + str(kindoftestping) + str(
            timeout) + str(times) + " at time " + time.strftime("%c"))
        if kindoftestdown == 1:
            download = s.download()
            download = download / 1024
            download = round(download)
            f.write("\nDownload Speed (" + str(timessofar) + "): " + str(download) + "KB/s. " + str(
                download / 1024) + "MB/s")
        if kindoftestping == 1:
            ping = s.lat_lon
            f.write("\nPing:" + str(ping))
        if kindoftestup == 1:
            if memorypreallocation == "Y":
                upload = s.upload(pre_allocate=False)
            elif memorypreallocation != "Y":
                upload = s.upload()
            upload = upload / 1024
            upload = round(upload)
            f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
        timessofar = timessofar + 1
        f.close


if status == 0:
    Button(mainwindow, text="Ready to run", command=lambda: test()).grid(row=7, column=0, sticky=NW)

mainwindow.mainloop()
