# Morgan Stimpson (morgan.stimpson@hotmail.com)
# piBrew 
##################################################################
#
#                        ######                       
#               #####  # #     # #####  ###### #    # 
#               #    # # #     # #    # #      #    # 
#               #    # # ######  #    # #####  #    # 
#               #####  # #     # #####  #      # ## # 
#               #      # #     # #   #  #      ##  ## 
#               #      # ######  #    # ###### #    # 
#
##################################################################

# This is intended to study and monitor the fermentation rate of wort

#import section
from datetime import datetime
from time import sleep, time

import signal # this is for signaling to store all when ctrl c is typed
import sqlite3
import pandas as pd
import os
from os import path

# ======================= SENSORS ========================================

# ReadFromSensors
def ReadFromSensors():
    
    print("-- pulling data from sensors.")

    temperature = pullTempReading()
    o2          = pullO2Reading()
    co2         = pullCO2Reading()
    ph          = pullPHReading()

    return temperature, o2, co2, ph

# This is the sensor section.
# I can not quiet read from these yet as I do not have a raspberry Pi to work with

# https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
def pullTempReading():
    temp = 0
    return temp

def pullO2Reading():
    o2 = 1
    return o2

def pullCO2Reading():
    co2 = 2
    return co2

def pullPHReading():
    ph = 3
    return ph

# Connect To Sensors
def ConnectToSensors():
    print("")
    print("FOOL OF A TOOK!")
    print("This has not been set up yet.")

    if(1 != 2):            # if unable to connect return -1 for a failure.
        return -1
    return 0

# ==========================================================================



# Write To DataBase
# - Write to a sql database 
# - fields include time, temp, o2, co2, ph, having a herculomitor reading would be rad to
def WriteToDB(connection, beerStyle, brewDate):

    temperature, o2, co2, ph = ReadFromSensors()

    print("")
    print("- Sucessfully read from sensors.")
    print("- trying to write")

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S") 

    sql =       """
                INSERT INTO FERMENTATION
                (STYLE, DATEBREWED, TIME, TEMPERATURE, O2, CO2, PH) \
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """

    # this is what allows us to use the values.
    # now going to insert variables in there and make params a tuple
    
    params = (beerStyle, brewDate, currentTime, temperature, o2, co2, ph)
    connection.execute (sql, params)
    connection.commit ()
    
    print("- Written to database")



# Repeat Function -- come up with a better name
# this function is what will be running once everything is started up.
# this will constantly but every 15 minutes it will kick in to write.
def RepeatFunction(connection, beerStyle, brewDate):
    print("")
    print("Starting data collection") 

    condition = False

    while datetime.now().minute not in {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}: 
        print("waiting until a multiple of 5 before we write")
        sleep(60) # this is in seconds, it will attempt to write every 1 minutes.
    
    def timer():
        print("")
        print("We are up and running")
        WriteToDB(connection, beerStyle, brewDate)
        # this is necessary since it will run in a near infinite loop and will crash. --stackoverflow error
        print("-Now sleeping")
        sleep(61)  # going to lean on the edge of 61 so we have no chance of calling 2 times inside of the same minute
        print("-Now going to repeat")
        RepeatFunction(connection, beerStyle, brewDate)

    timer()



# Main
# this is the central operator of the entire program
# [] need to connect to the database then close
# [] need to run the timing service
# [] need to pull data correctly
def main():
    print("Howdy, first we are going to set up the data base for you boss.")
    print("One second please.")

    
    connection = sqlite3.connect('fermentation.db') # this will make a db if none are found -- if there is one skip
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

    if(cursor.fetchall() == ()):
        print("Making table!")

        connection.execute ('''CREATE TABLE FERMENTATION
                (   STYLE           STR,
                DATEBREWED      STR,
                TIME            TIME PRIMARY KEY     NOT NULL,
                TEMPERATURE     INT,
                O2              INT,
                CO2             INT,
                PH              INT);''')

    

    print("Connected to database correctly.")

    # TODO: Take in user input to reattempt
    if(ConnectToSensors() == -1):
        print("Sensors failed to connect.")
        print("Would you like to retry?")
    else:
        print("Sensors are connected correctly")

    # user input section
    beerStyle = input("Enter the style of your beer: ") 
    brewDate  = input("Please enter date of brew in the format of --.--.---- ")
    print("Thank you. Begining study.")

    WriteToDB(connection, beerStyle, brewDate)
    sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)
    # sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)


    # This is used to see what is up there. RAAAD

    cursor = connection.execute("SELECT STYLE, DATEBREWED, TIME, TEMPERATURE, O2, CO2, PH from FERMENTATION")
    
    for row in cursor:
       print ("STYLE = ", row[0])
       print ("DATEBREWED = ", row[1])
       print ("TIME = ", row[2])
       print ("TEMPERATURE = ", row[3])
       print ("O2 = ", row[4])
       print ("CO2 = ", row[5]) 
       print ("PH = ", row[6], "\n")

    #RepeatFunction(connection, beerStyle, brewDate)

    # When function is ended I want all to save and look back at it
    connection.close() # don't forget to close the db when you're finsihed


if __name__ == '__main__':
    main()
