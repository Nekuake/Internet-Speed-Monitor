# Script done by Nekuake using Sivel's speedtest.
import time
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

kindoftestdown = IntVar()
kindoftestup = IntVar()
kindoftestping = IntVar()
memorypreallocation = IntVar()

Checkbutton(mainwindow, text="Download", variable=kindoftestdown).grid(row=3, column=0, sticky=NW)
Checkbutton(mainwindow, text="Upload", variable=kindoftestup).grid(row=3, column=1, sticky=NW)
Checkbutton(mainwindow, text="Ping", variable=kindoftestping).grid(row=3, column=2, sticky=NW)
Checkbutton(mainwindow, text="Disable Mem. preallocation.", variable=memorypreallocation).grid(row=3, column=3,
                                                                                               sticky=SW)
def test():
    global times, kindoftestping, kindoftestdown, kindoftestdown, kindoftestping, timeout, status, mainwindow
    print("Starting test function...")
    mainwindow.withdraw()
    timesdef = int(times.get())
    timeoutdef = int(timeout.get())
    timessofar = 1
    kindoftestpingdef=kindoftestping.get()
    kindoftestdowndef=kindoftestdown.get()
    kindoftestupdef=kindoftestup.get()
    resultwindow = Tk()
    resultwindow.tk.call('tk', 'scaling', 2.0)
    resultwindow.geometry('500x300')
    resultwindow.configure(bg="#F0F0F0")
    resultwindow.title("Internet Speed Monitor-Results")
    Label(resultwindow, text="Results").grid(row=0, column=0, sticky=NW)
    resultwindow.update()
    while timessofar <= timesdef:
        f = open("outputgui.txt", "a")
        if timessofar == 1:
            print("Getting best server...")
            s.get_best_server()
            print("Best server acquired!")
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
        if kindoftestdowndef == 1:
            download = s.download()
            download = download / 1024
            download = round(download)
            Label(resultwindow, textvariable=download).grid(row=1, column=0, sticky=NW)
            resultwindow.update()

            f.write("\nDownload Speed (" + str(timessofar) + "): " + str(download) + "KB/s. " + str(
                download / 1024) + "MB/s")
        if kindoftestpingdef == 1:
            ping = s.lat_lon
            f.write("\nPing:" + str(ping))
            print("\nPing:" + str(ping))
            Label(resultwindow, textvariable=str(ping)).grid(row=1, column=2, sticky=NW)
            resultwindow.update()

        if kindoftestupdef == 1:
            if memorypreallocation == "Y":
                upload = s.upload(pre_allocate=False)
            elif memorypreallocation != "Y":
                upload = s.upload()
            upload = upload / 1024
            upload = round(upload)
            Label(resultwindow, textvariable=upload).grid(row=1, column=1, sticky=NW)
            resultwindow.update()

            f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
        timessofar = timessofar + 1
        f.close
        resultwindow.update()


Label(mainwindow, text="Nº of tests").grid(row=4, column=0, sticky=NW)
times = Spinbox(mainwindow, width=10, from_=1, to=9999)
times.grid(row=4, column=1, sticky=NW)
Label(mainwindow, text="Seconds").grid(row=4, column=2, sticky=NW)
timeout = Spinbox(mainwindow, width=10, from_=1, to=9999)
timeout.grid(row=4, column=3, sticky=NW)
if status == 0:
    Label(mainwindow, text="OK. Waiting conf.", fg="green").grid(row=5, column=0)
else:
    Label(mainwindow, text="INSTALL THE SPEEDTEST PYTHON MODULE", fg="red").grid(row=5, column=0, sticky=NW)
if status == 0:
    Button(mainwindow, text="Ready to run", command=lambda: [test() ]).grid(row=7, column=0, sticky=NW)
mainwindow.mainloop()






