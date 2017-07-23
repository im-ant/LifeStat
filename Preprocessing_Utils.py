"""############################################################################


############################################################################"""

import csv
import datetime

#Anaconda-dependent packages
import numpy as np
import pandas as pd


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
def typeConvert_sleepbot_entry(logRow):
    #Convert the date, sleeptime and
    #Convert the sleeptime to a proper datetime

    #Convert the waketime to a proper datetime
    #Convert the duration to a proper duration
    #Convert the rating to an integer
    #Convert the date a proper date (maybe shift)
    #Add things to a list and return
    return None #TODO: temp return


# ===========================================================================
# Function to read a .csv file from the sleepbot website, convert the values
# into appropriate types and save into a pandas.dataframe
#
# Input:
#   - path: path to the .csv file
# Output:
#   - pandas.dataframe containing sleep data in the following format:
#       pre-sleep date, sleep date-time, awake date-time, duration, rating
# ===========================================================================
def read_sleepbot_logs(path):
    #Open the file and read
    log_inStream = open(path, 'rb')
    logReader = csv.reader(log_inStream)

    #Save as list!
    print "eyo"

    for row in logReader:
        print row
        print len(row)
        print typeConvert_sleepbot_entry(row)
        break
        #Convert row to proper type
        #Append the row to a dataframe
        #

    #Close the file
    log_inStream.close()



#TODO; delete below
read_sleepbot_logs('data/SleepBot_Log_20131217-20170720.csv')
print str2timedelta('07 hr 35 min')
