# Script done by Nekuake using Sivel's speedtest.
import time

# Tbe name of the variables used in this script
times = 0
timeout = 0
timessofar = 0
download = 0
upload = 0
ping = 0
kindoftest = 0
testping = 0
# Let's start
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
print("There shouldn't be any error, but if you have MemoryError, you should answer yes: \n")
memorypreallocation = input("Disable memory preallocation? (press enter= no/ press Y = yes) >> ").upper()

s.get_best_server()
print("Set the values:")
times = input("Number of times: >> ")
timeout = input("How many seconds between every test: >> ")
kindoftest = input("0 for upload and download speed, 1 for just download, 2 for just upload.")
testping = input("Test ping? (0/1)")
while timessofar != times:
    if kindoftest == 0 or 1:
        download=s.download()
    if kindoftest == 1:
        ping= s.lat_lon
    if kindoftest == 0 or 2:
        if memorypreallocation == "Y":
            upload = s.upload(pre_allocate=False)
        elif memorypreallocation != "Y":
            upload = s.upload()
        if ping != 0:
            print(ping)
        if download != 0:
            print(download)
        if upload != 0:
            print(upload)
    #with open("Result.txt", "w") as  text_file:
     #   print= (s.download(), file = result.txt)

      #  time.sleep(timeout)
