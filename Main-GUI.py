# Script done by Nekuake using Sivel's speedtest.
import time
import threading
from tkinter import *
from tkinter.ttk import *
try:
    import speedtest

    print("Package found! Ready to run!")
    s = speedtest.Speedtest()  # Used
    status = 0
except ImportError as e:  # Package not found, scipt shouldn't be run
    status = -1
download = 0
upload = 0
ping = 0
timewaited = 0
timessofar = 0
running = 0
mainwindow = Tk()
mainwindow.tk.call('tk', 'scaling', 2.0)
mainwindow.geometry('550x120')
mainwindow.configure(bg="#F0F0F0")
mainwindow.title("Internet Speed Monitor")

kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()

guidownloadcheck = Checkbutton(mainwindow, text="Download", variable=kindoftestdown)
guidownloadcheck.grid(row=3, column=0, sticky=NW)
guiuploadcheck = Checkbutton(mainwindow, text="Upload", variable=kindoftestup).grid(row=3, column=1, sticky=NW)
guipingcheck = Checkbutton(mainwindow, text="Ping", variable=kindoftestping).grid(row=3, column=2, sticky=NW)
guiprealloccheck = Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation).grid(row=3, column=3,
                                                                                               sticky=SW)
Label(mainwindow, text="Nº of tests").grid(row=4, column=0, sticky=NW)

times = Spinbox(mainwindow, width=10, from_=1, to=9999)
times.grid(row=4, column=1, sticky=NW)
Label(mainwindow, text="Seconds").grid(row=4, column=2, sticky=NW)
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999)
timeout.grid(row=4, column=3, sticky=NW)


def test():
    global running
    if running ==0:
        running = 1
        print("Starting test function...")
        timesdef = int(times.get())
        timeoutdef = int(timeout.get())
        timessofar = 1
        timewaited = 0
        kindoftestpingdef = kindoftestping.get()
        kindoftestdowndef = kindoftestdown.get()
        kindoftestupdef = kindoftestup.get()
        while timessofar <= timesdef:
            f = open("outputgui.txt", "a")
            if timessofar == 1:
                print("Getting best server...")
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
                print("Waiting", str(timeout), " seconds...")

                while timewaited != timeoutdef:
                    time.sleep(1)
                    timewaited = timewaited + 1
            f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
                timessofar) + "/" + str(times) + ": " + str(kindoftestdown) + str(kindoftestup) + str(kindoftestping) + str(
                timeout) + str(times) + " at time " + time.strftime("%c"))
            if kindoftestdowndef == 1:
                download = s.download()
                download = download / 1024
                download = round(download)
                f.write("\nDownload Speed (" + str(timessofar) + "): " + str(download) + "KB/s. " + str(
                    download / 1024) + "MB/s")
                download = str(download)

            if kindoftestpingdef == 1:
                ping = s.lat_lon
                f.write("\nPing:" + str(ping))
                print("\nPing:" + str(ping))
                ping = str(ping)

            if kindoftestupdef == 1:
                if memorypreallocation == "Y":
                    upload = s.upload(pre_allocate=False)
                elif memorypreallocation != "Y":
                    upload = s.upload()
                upload = upload / 1024
                upload = round(upload)
                print("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
                f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
                upload = str(upload)

            timessofar = timessofar + 1

            print(round((timessofar/timesdef)*100))
            f.close
            timewaited = 0



guirun = Button(mainwindow, text="Run", command=lambda: [threading.start_new_thread(test())])
guirun.grid(row=5, column=0, sticky=NW)
mainwindow.mainloop()
