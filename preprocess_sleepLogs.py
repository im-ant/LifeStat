#Script to pre-process the sleep input

import sys
import csv
import datetime
import SleepBot_Utils as SB


PATH = 'data/SleepBot_Log_20131217-20170720.csv'
SUNKENDAY_PATH = 'data/Sunken_Days_20170104-20170723.csv'
#Initialize the list to store all the data
sleep_data_list = []

#Open the file and read
log_inStream = open(PATH, 'rb')
logReader = csv.reader(log_inStream)

#Iterate through all rows of the input file to store data
for row in logReader:
    #Strip the elements of pre-existing quotes
    str_row = [ entry.strip('\'').strip('\"') for entry in row ]
    #Skip header
    if 'Date' in str_row:
        continue

    #Convert the current row to proepr types
    log_data = SB.typeConvert_sleepbot_rowEntry(str_row)

    #Add the row to the list
    sleep_data_list.append(log_data)

#Close the file
log_inStream.close()

#User indication
print "Done reading input file. %d sleep logs acquired." % len(sleep_data_list)

#Collapse
colla_list = SB.collapse_repeated_dates(sleep_data_list)

print "Collapsed list length: %d " % len(colla_list)

#Get the sunday days (positive examples)
sunken_list = []
with open(SUNKENDAY_PATH, 'rb') as sunken_instream:
    sunkenReader = csv.reader(sunken_instream)
    for row in sunkenReader:
        #Skip first row
        if 'Date' in row: continue
        #Initialize the date in all other rows
        d = SB.str2date(row[0])
        sunken_list.append(d)
print "Sunken days initiated: %d" % len(sunken_list)

#Variable to store analysi
data = []
#Get a list of all the days present
#Get dates that are in 2017 and have at least two days before it
for i in range(0, len(sleep_data_list)-2):
    #Get the current date
    cur_date = sleep_data_list[i][0]

    #Skip data that isn't in 2017
    if cur_date.year != 2017:
        continue

    #Get the dates we need to initialize the training set
    d1 = cur_date - datetime.timedelta(days=1)
    d2 = cur_date - datetime.timedelta(days=2)
    #Are the data available?
    if sleep_data_list[i+1][0] != d1:
        continue
    if sleep_data_list[i+2][0] != d2:
        continue

    #If so, initialize variable via converting duration to hours
    x1 = sleep_data_list[i+1][3].total_seconds() / 3600.0
    x2 = sleep_data_list[i+2][3].total_seconds() / 3600.0
    datapoint = [x1, x2]
    #See if it is a positive/negative example
    if cur_date in sunken_list:
        datapoint.append(1)
    else:
        datapoint.append(0)

    data.append(datapoint)

print "Training set size: %d" % (len(data))

print "Importing numpy..."

import numpy as np

print "Saving matrix..."
np.save('data/temp_data.npy',np.array(data))
print "Done"
