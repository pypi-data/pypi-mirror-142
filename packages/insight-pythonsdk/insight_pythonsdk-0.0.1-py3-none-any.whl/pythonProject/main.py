# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
import mmap
import time
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    filemaxsize = 1073741824
    fileindex = 0;
    filereadsize = 0;
    tempfilesize = 4;
    filename = 'D:\\data.dat'
    filefd = os.open(filename, os.O_RDWR)
    start = time.perf_counter_ns()
    data = mmap.mmap(filefd, filemaxsize, access=mmap.ACCESS_READ)
    end = time.perf_counter_ns()
    print('time out',end-start)
    #while True:

    flag = 0x02ff43ee
    endflag =0x0856dd78
    fileCount = 0
    fileCountAll = 0
    timeave = 0

    start = 0


    indexname = 'D:\\index.dat'
    maxtimespan = 0
    indexfd = os.open(indexname, os.O_RDWR)
    index = mmap.mmap(indexfd, 24, access=mmap.ACCESS_READ)

    test = [x for x in range(10)]
    print(test[0:4])
    test = [x for x in range(10)]
    print(test[0:4])
    while True:
        #os.lseek(indexfd, 0, 0)
        #index = mmap.mmap(indexfd, 24, access=mmap.ACCESS_READ)
        filewritesize = int.from_bytes(index[0:8], byteorder='big', signed=False)
        #filewritesize = index.read(4)
        #print(index[0:8],filewritesize)
        tempflagsize = filereadsize+4;

        if filereadsize!=filewritesize:

            tempflag = int.from_bytes(data[filereadsize:tempflagsize],byteorder='big', signed=False)
            #print(tempflag)
            if flag==tempflag:
                #start = time.perf_counter_ns()
                tempfilesize = filereadsize + 8
                #print('tempfilesize:', tempfilesize, end="@@")
                filesize = int.from_bytes(data[tempflagsize:tempfilesize],byteorder='big', signed=False)

                tempflagsize = tempfilesize
                tempfilesize = filereadsize + 12
                temptime = int.from_bytes(data[tempflagsize:tempfilesize], byteorder='big', signed=False)
                timespan = time.monotonic_ns()/1000000-temptime
                if start == 1:

                    if  fileCountAll>0:
                        timeave = (timespan+timeave*fileCountAll)/(fileCountAll+1)
                    fileCountAll += 1
                    if timespan>maxtimespan:
                        print(filewritesize - filereadsize,timespan)
                        maxtimespan = timespan
                #print(temptime,time.monotonic_ns())

                tempfileend = tempfilesize+filesize
                tempbyte = data[tempfilesize:tempfileend]
                tempstr = tempbyte.decode("utf-8",errors = 'ignore')
                #print(tempstr)
                #dict = eval(tempstr)
                #print(dict)
                #print('filesize:', filesize, end="~~")
                filereadsize = filereadsize+filesize+12
                #end = time.perf_counter_ns()
                fileCount +=1

                if fileCount == 10000:
                    start = 1
                    fileCount = 0
                if fileCount == 0:
                    print(filereadsize,filewritesize,maxtimespan,timespan,timeave)

            elif endflag == tempflag:
                filereadsize=0
                print(fileCount,'******************************************************************')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
