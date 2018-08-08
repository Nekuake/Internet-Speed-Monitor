# Script done by Nekuake using Sivel's speedtest.
import time
import os
import math

print("This script needs that you have installed previously the speedtest package.\n")
print("Please, be sure that you have it first.\n")
try:
    import speedtest
    print("Package found! Ready to run!")
    s = speedtest.Speedtest()  # Used
except ImportError as e:  # Package not found, scipt shouldn't be run
    print("Speedtest package hasn't been found. Closing...")
    input("Press any key...")
    exit()
print("If you have MemoryError, you should answer yes. Otherwise, just press enter: \n")
memorypreallocation = input("Disable memory preallocation? (press enter= no/ press Y = yes) >> ").upper()
print("Set the values:")
infinitesting = int(input("Infinite testing?(0/1) >>"))
if infinitesting == 1:
    times = math.inf
else:
    times = int(input("Number of times: >> "))
timeout = int(input("How many seconds between every test: >> "))
kindoftestdown = int(input("Test download speed? (0/1)"))
kindoftestup = int(input("Test upload speed? (0/1)"))
testping = int(input("Test ping? (0/1)"))
if os.path.isfile("output.txt"):
    remove = input("OLD OUTPUT FILE FOUND, DELETE IT?(Y or any other key) >> ").upper()
    if remove == "Y":
        os.remove("output.txt")
timessofar = 1
if timeout == 0:
    timeout = 1
    print("TIMEOUT MUST BE 1 SECOND AT LEAST...")
while timessofar <= times:
    f = open("output.txt", "a")
    if timessofar == 1:
        print("DO NOT CLOSE THE WINDOW OR THE TEST WILL HALT!")
        print("Connecting to the closest server...")
        print("USING SERVER:\n" , s.get_best_server())
        print('TEST RUN AT: ', time.strftime("%c") + " with serial " + str(times) + str(kindoftestup) + str(kindoftestdown) + str(testping) + str(timeout))
        f.write("\n" + "TEST RUN AT: " + time.strftime("%c") + "with serial" + str(times) + str(kindoftestup) + str(kindoftestdown) + str(testping) + str(timeout))
    else:
        print("Waiting", timeout, " seconds...")
        time.sleep(timeout)
    print("\n------------------------------------------------------------------------------------------------")
    print("TEST NUMBER", timessofar, "/", times, ":", kindoftestdown, kindoftestup, testping, timeout, times, "at time", time.strftime("%c") )
    f.write("\n" + "\n-----------------------------------------------------------" + "\nTEST NUMBER " + str(
        timessofar) + "/" + str(times) + ": " + str(kindoftestdown) + str(kindoftestup) + str(testping) + str(
        timeout) + str(times) + " at time " + time.strftime("%c"))
    if kindoftestdown == 1:
        print("Testing download speed...(", timessofar, ")/(", times, ")")
        download = s.download()
        download = download / 1024
        download = round(download)
        print("Download Speed (", timessofar, "): ", download, "KB/s. ", download / 1024, "MB/s")
        f.write("\nDownload Speed ("+ str(timessofar)+ "): "+ str(download) + "KB/s. "+ str(download / 1024)+ "MB/s")
    if testping == 1:
        print("Testing ping...(", timessofar, ")")
        ping = s.lat_lon
        print("Ping:" , ping)
        f.write("\nPing:" + str(ping))
    if kindoftestup == 1:
        print("Testing upload speed...(", timessofar, ")")
        if memorypreallocation == "Y":
            upload = s.upload(pre_allocate=False)
        elif memorypreallocation != "Y":
            upload = s.upload()
        upload = upload / 1024
        upload = round(upload)
        print("Upload Speed (", timessofar, "): ", upload, "KB/s. ", upload / 1024, "MB/s")
        f.write("\nUpload Speed (" + str(timessofar) + "): " + str(upload) + "KB/s. " + str(upload / 1024) + "MB/s")
    print("TEST FINISHED...")
    timessofar = timessofar + 1
    f.close
print("Schelude completed. Check the output file.")
input()
