# Script done by Nekuake using Sivel's speedtest.
import time
import os
import math
import pprint
import errno
import json
pp = pprint.PrettyPrinter(indent=4)
print("Internet Speed Monitor is a program that tests the Internet Speed. Done by Nekuake")
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
timessofar = 1
try:
    os.makedirs("Logs")
    print("Folder created!!")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
if timeout == 0:
    timeout = 1
    print("TIMEOUT MUST BE 1 SECOND AT LEAST...")
dirname = os.path.dirname(__file__)
filename= os.path.join(dirname, "Logs/CLI_TEST_" + time.strftime("%Y-%m-%d_%H-%M-%S")+"_CLI.txt")
while timessofar <= times:
    f = open(filename, "a")
    if timessofar == 1:
        print("DO NOT CLOSE THE WINDOW OR THE TEST WILL HALT!")
        print("Connecting to the closest server...")
        serverdata = (s.get_best_server())
        f.write(json.dumps(serverdata))
        print("USING SERVER:" )
        for x, y in serverdata.items():
            print(x, ": ", y)
        print (serverdata)
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
    f.close()
if times == 0:
    print("No tests will be executed...")
else:
    print("Schelude completed. Check " + filename)
input()

