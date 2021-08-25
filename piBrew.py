# Morgan Stimpson (morgan.stimpson@hotmail.com)
# 
# piBrew
# This is intended to study and monitor the fermentation rate of beer currently brewing.

#import section
from datetime import datetime
from time import sleep, time

import sqlite3
import pandas as pd

# Connect To Sensors
def ConnectToSensors():
    print("bah")

    if(1 == 2):            # if unable to connect return -1 for a failure.
        return -1

    return 0

# ReadFromSensors
def ReadFromSensors():
    
    print("-- connecting to sensors.")

# WriteToDB
# Write to a sql database 
# fields include time, temp, o2, co2, ph, having a herculomitor reading would be rad to
def WriteToDB(con):

    ReadFromSensors()

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S") 
    valuesToInsert = (currentTime, 0, 1, 2, 3)

    # https://stackoverflow.com/questions/11712342/inserting-a-variable-to-the-database-using-sqlite-in-python
    # need to figure out the way to send variables in. -- tuple?
    con.execute ("INSERT INTO FERMENTATION (TIME, TEMPERATURE, O2, CO2, PH) \
                VALUES ()", valuesToInsert)
    con.commit ()

    # cursor = con.execute("SELECT TIME, TEMPERATURE, O2, CO2, PH from FERMENTATION")
    # for row in cursor:
    #    print ("TIME = ", row[0])
    #    print ("TEMPERATURE = ", row[1])
    #    print ("O2 = ", row[2])
    #    print ("CO2 = ", row[3]) 
    #    print ("PH = ", row[4], "\n")

    
    print("- trying to write")
    print("- Current Time =", currentTime)
    print("- written")


# Repeat Function -- come up with a better name
# this function is what will be running once everything is started up.
# this will constantly but every 15 minutes it will kick in to write.
def RepeatFunction(con):

    condition = False

    while datetime.now().minute not in {0, 15, 30, 45}: 
        print("waiting 15 minutes before we write")
        sleep(60) # this is in seconds, it will attempt to write every 1 minutes.
    
    def timer():
        print("We are up and running")
        WriteToDB(con)
        # this is necessary since it will run in a near infinite loop and will crash. --stackoverflow error
        sleep(60) 
        RepeatFunction()

    timer()



# Main
# this is the central operator of the entire function
# [] need to connect to the database then close
# [] need to run the timing service
def main():
    print("howdy, first we are going to set up the data base.")
    print("one second please.")
    
    # HECK YEAH DUDE IT'S GOING GOOD

    con = sqlite3.connect('fermentation.db') # this will make a db if none are found -- if there is one skip
    print("Connected to server correctly")

    con.execute ('''CREATE TABLE FERMENTATION
                (TIME           TIME PRIMARY KEY     NOT NULL,
                 TEMPERATURE    INT,
                 O2             INT,
                 CO2            INT,
                 PH             INT);''')

    # con.execute ("INSERT INTO FERMENTATION (TIME, TEMPERATURE, O2, CO2, PH) \
    #   VALUES (0, 0, 0, 0, 0)")
    # con.commit ()
    # 
    # cursor = con.execute("SELECT TIME, TEMPERATURE, O2, CO2, PH from FERMENTATION")
    # for row in cursor:
    #    print ("TIME = ", row[0])
    #    print ("TEMPERATURE = ", row[1])
    #    print ("O2 = ", row[2])
    #    print ("CO2 = ", row[3]) 
    #    print ("PH = ", row[4], "\n")

    # data = pd.write           # ooop don't know what to do with this.

    # DB IS WORKING!

    if(ConnectToSensors() == -1):
        print("Sensors failed to connect.")
        print("Would you like to retry?")
    else:
        print("Sensors are connected correctly")


    print("starting data collection")

    RepeatFunction(con)

    # When function is ended I want all to save and look back at it

    con.close() # don't forget to close the db when you're finsihed


if __name__ == '__main__':
    main()
