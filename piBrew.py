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
from time import sleep
import RPi.GPIO as GPIO

import sqlite3
#import pandas as pd

# ======================= SENSORS ========================================

# Read From Sensors
# Here we pull the data from the sensors
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
# If we are unable to connect to the sensors then return -1
#  If we are able to connect return 0
def ConnectToSensors():
    print("")
    print("This has not been set up yet.")

    if(1 != 2):
        return -1
    return 0

# ==========================================================================



# Write To DataBase
# - Write to a sql database 
# - fields include style, datebrewed, time, temp, o2, co2, ph, 
#   having a herculomitor reading would be rad to
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

    params = (beerStyle, brewDate, currentTime, temperature, o2, co2, ph)
    connection.execute (sql, params)
    connection.commit ()
    
    print("- Written to database")



# Repeat Function -- come up with a better name
# this function is what will be running once everything is started up.
# this will constantly but every 5 minutes it will kick in to write.
# Once it is ran it will sleep for 1 minute and 1 second 
#    so that it does not write 2 times on the same minute
def RepeatFunction(connection, beerStyle, brewDate):
    print("")
    print("Starting data collection") 

    while( datetime.now().minute not in {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}): 
        print("waiting until a multiple of 5 before we write")
        sleep(60)
    
    def timer():
        print("")
        print("We are up and running")
        WriteToDB(connection, beerStyle, brewDate)
        print("-Now sleeping")
        sleep(61)
        print("-Now going to repeat")
        RepeatFunction(connection, beerStyle, brewDate)

    timer()



# Main
# this is the central operator of the entire program
# [x] need to connect to the database then close
# [x] need to run the timing service
# [x] need to pull data correctly
def main():
    print("Howdy, first we are going to set up the data base for you boss.")
    print("One second please.")

    
    connection = sqlite3.connect('fermentation.db') # this will make a db if none are found -- if there is one skip
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    a = cursor.fetchall()

    if not a: 
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
        print("You should restart the program.")
    else:
        print("Sensors are connected correctly")

    # user input section
    # on the raspbian side it fails if it does not have "" around the input
    print("Please write your inputs within qoutes. Working on a way to fix that thank you.")
    beerStyle = input("Enter the style of your beer: ") 
    brewDate  = input("Please enter date of brew in the format of --.--.---- ")
    print("Thank you. Begining study.")

    
    #===========TESTING=======================
    # 
    # WriteToDB(connection, beerStyle, brewDate)
    # sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)
    # sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)
    # 
    # This is used to see what is up there. RAAAD
    # 
    # cursor = connection.execute("SELECT STYLE, DATEBREWED, TIME, TEMPERATURE, O2, CO2, PH from FERMENTATION")
    # 
    # for row in cursor:
    #    print ("STYLE = ", row[0])
    #    print ("DATEBREWED = ", row[1])
    #    print ("TIME = ", row[2])
    #    print ("TEMPERATURE = ", row[3])
    #    print ("O2 = ", row[4])
    #    print ("CO2 = ", row[5]) 
    #    print ("PH = ", row[6], "\n")
    # 
    # When runnning on the pi it has u sitting in front of the data inserted. 
    # believe it has to do with raw_input vs input issue
    # odd
    #=========================================

    RepeatFunction(connection, beerStyle, brewDate)

    # When function is ended I want all to save and look back at it
    connection.close() # don't forget to close the db when you're finsihed


if __name__ == '__main__':
    main()
