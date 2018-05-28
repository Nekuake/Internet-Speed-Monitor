# Script done by Nekuake using Sivel's speedtest.
import time
import decimal

timessofar = (0)
times = 0
ping = 0
download = 0
upload = 0

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
times = int(input("Number of times: >> "))
timeout = int(input("How many seconds between every test: >> "))
kindoftestdown = int(input("Test download speed? (0/1)"))
kindoftestup = int(input("Test upload speed? (0/1)"))
testping = int(input("Test ping? (0/1)"))
while timessofar < times:
    if timessofar == 0:
        s.get_best_server()
    else:
        time.sleep(timeout)
    timessofar = timessofar + 1
    if kindoftestdown == 1:
        print("Testing download speed...(", timessofar, ")/(" , times, ")")
        download = s.download()
        download = download / 1024
        download = round(download)
        print("Download Speed (", timessofar, "): ", download, "KB/s. ", download/1024 , "MB/s")
    if testping == 1:
        print("Testing ping...(", timessofar, ")")
        ping = s.lat_lon
        print(ping)
    if kindoftestup == 1:
        print("Testing upload speed...(", timessofar, ")")
        if memorypreallocation == "Y":
            upload = s.upload(pre_allocate=False)
        elif memorypreallocation != "Y":
            upload = s.upload()
        upload = upload / 1024
        upload = round(upload)
        print("Upload Speed (", timessofar, "): ", upload, "KB/s. ", upload / 1024, "MB/s")
print("Schelude completed. Check the output file.")
# with open("Result.txt", "w") as  text_file:
#   print= (s.download(), file = result.txt)

#  time.sleep(timeout)
