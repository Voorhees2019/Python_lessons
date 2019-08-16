#!/bin/python3
# putge_log logfile.txt 10 5
import os, sys, shutil

if len(sys.argv) < 4:
    print('Missing argument! (Usage sctipt.py max_size(kilobytes) max_amount_of_copied_logfiles')
    exit(1)

file_name = sys.argv[1]
limit_size = sys.argv[2]
logs_number = sys.argv[3]
if os.path.isfile(file_name):                  # if main logfile exists
    logfile_size = os.stat(file_name).st_size  # get logfile size(in kilobytes)
    logfile_size /= 1024                       # convert size to bytes
    if logfile_size >= limit_size:
        if logs_number > 0:
            for current_file_number in range(logs_number, 1, -1):
                src = file_name + "_" + str(current_file_number-1)
                dest = file_name + "_" + str(current_file_number)
                if (os.path.isfile(src) == True):
                    shutil.copyfile(src, dest)
                    print('Copied: ' + src + " to " + dest)
            shutil.copyfile(file_name, file_name + "_1")
            print('Copied ' + file_name + ' to ' + file_name + '_1')
        my_file = open(file_name, 'w')
        my_file.close()
