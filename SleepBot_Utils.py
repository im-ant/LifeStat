"""############################################################################


############################################################################"""

import csv
import datetime


# ===========================================================================
# Helper function turn a string into a datetime.date object
#
# Input:
#   A string with format "yyyy-mm-dd"
#
# Output:
#   A datetime.date object that describes the date
# ===========================================================================
def str2date(str_date):
    #Split the string into its components and convert to int
    date_parts = [ int(part) for part in str_date.split('-') ]
    #Turn it into a datetime object
    d = datetime.date(date_parts[0], date_parts[1], date_parts[2])
    return d


# ===========================================================================
# Helper function turn a string into a datetime.time object
#
# Input:
#   A string with format "hour:min am/pm"
#
# Output:
#   A datetime.time object that describes the time
# ===========================================================================
def str2time(str_time):
    #Split the string into hours and minutes, while converting to integers
    hour_min = [ int(part) for part in str_time.split(' ')[0].split(':') ]
    #See if the hour is in pm
    if str_time.split(' ')[1].strip() == 'pm':
        hour_min[0] += 12
    #Convert the integer list to a time object
    t = datetime.time(hour_min[0], hour_min[1])
    return t


# ===========================================================================
# Helper function turn a string into a datetime.timedelta object
#
# Input:
#   A string with format "[hh] hr [mm] min"
#
# Output:
#   A datetime.timedelta object that describes the time duration
# ===========================================================================
def str2timedelta(str_duration):
    #Split the duration and initialize hour:min information
    dur = [ int(str_duration.split(' ')[0]) , int(str_duration.split(' ')[2]) ]
    #Initialize datetime object
    time_d = datetime.timedelta(hours=dur[0], minutes=dur[1])
    return time_d


# ===========================================================================
# Helper function to read_sleepbot_logs, which takes in a single entry (list)
# from the sleepbot imput csv and converts it to its proper types
#
# Input:
#   A list containing the date, sleep time, awake time, during and rating str
#
# Output:
#   A list containing the same information, but in proper type. Note that the
#   date may be changed based on the sleeptime
# ===========================================================================
def typeConvert_sleepbot_rowEntry(logRow):
    #Convert the log date to a datetime.date
    log_date = str2date(logRow[0])
    #Convert the sleep and wake times to a datetime.time
    sleep_time = str2time(logRow[1])
    awake_time = str2time(logRow[2])
    #Convert the duration to a datetime.timedelta
    duration = str2timedelta(logRow[3])
    #Try to convert the rating to an integer, else return a None
    try:
        rating = int(logRow[4])
    except ValueError:
        rating = None
    #Return list with proepr variables
    return [log_date, sleep_time, awake_time, duration, rating]


# ===========================================================================
# Function to collapse multiple logs the same date into the same log
#   It assumes that the list is ordered, going latest date --> oldest date
#
# ===========================================================================
def collapse_repeated_dates(data_list):
    #Initialize a new list to return
    collapsed_list = []
    #Iterate through the list
    i = 0
    while (i < len(data_list)):
        #Check to see if the next entries have the same date
        rep = 1
        while (i+rep < len(data_list) ) and (data_list[i][0]==data_list[i+rep][0]):
            rep += 1
        #If so, collapse them together
        if rep > 1:
            #Append the date
            newlog = [ data_list[i][0] ]
            #Append the earliest sleeptiem
            newlog.append(data_list[i+rep-1][1])
            #Append the latest awake time
            newlog.append(data_list[i][2])
            #Add-up and append the sum of all the sleep durations
            tot_duration = data_list[i][3]
            for j in range(1,rep):
                tot_duration += data_list[i+j][3]
            newlog.append( tot_duration )
            #Append the latest rating
            newlog.append(data_list[i][4]) #TODO: fix the appending of ratings

            #Add the newest log to the new list
            collapsed_list.append(newlog)

        #Else, just add the current list to the new list
        else:
            collapsed_list.append(data_list[i])

        #Shift forward the counter and conintue
        i += rep

    #Replace the datalist with the new list
    return collapsed_list


# ===========================================================================
# Function to read a .csv file from the sleepbot website, convert the values
# into appropriate types and save into a nested list
#
# TODO: this is an incomplete function
#
# Input:
#   - path: path to the .csv file
# Output:
#   - ???
# ===========================================================================
def read_sleepbot_logs(path):
    #Initialize the list to store all the data
    sleep_data_list = []

    #Open the file and read
    log_inStream = open(path, 'rb')
    logReader = csv.reader(log_inStream)

    #Iterate through all rows of the input file to store data
    for row in logReader:
        #Strip the elements of pre-existing quotes
        str_row = [ entry.strip('\'').strip('\"') for entry in row ]
        #Skip header
        if 'Date' in str_row:
            continue

        #Convert the current row to proepr types
        log_data = typeConvert_sleepbot_rowEntry(str_row)

        #Add the row to the list
        sleep_data_list.append(log_data)

    #Close the file
    log_inStream.close()

    #User indication
    print "Done reading input file. %d sleep logs acquired." % len(sleep_data_list)

    #Collapse
    colla_list = collapse_repeated_dates(sleep_data_list)

    print len(colla_list)
