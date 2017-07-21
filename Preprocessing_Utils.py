"""############################################################################


############################################################################"""

import csv

#Anaconda-dependent packages
import numpy as np
import pandas as pd


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
        break
        #Convert row to proper type
        #Append the row to a dataframe
        #

    #Close the file
    log_inStream.close()

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
    #Convert the sleeptime to a proper datetime
    #Convert the waketime to a proper datetime
    #Convert the duration to a proper duration
    #Convert the rating to an integer
    #Convert the date a proper date (maybe shift)
    #Add things to a list and return
    return None #TODO: temp return

#TODO; delete below
read_sleepbot_logs('data/SleepBot_Log_20131217-20170720.csv')
