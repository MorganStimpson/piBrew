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

# GOAL: This function is intended to monitor the fermentation rate of beer.
# This software runs on a raspberry pi attached to a temperature sensor
# It will pull data and place it into a database for future use.

# IMPORT SECTION
from glob import glob
import sqlite3
import os
import glob
import time

from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

# GLOBALS
# # Therm
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
# # Lights
RLEDPin = 17
GLEDPin = 27
BLEDPin = 22

# Setup the pin the LED is connect to
GPIO.setup(RLEDPin, GPIO.OUT)
GPIO.setup(GLEDPin, GPIO.OUT)
GPIO.setup(BLEDPin, GPIO.OUT)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# ======================= SENSORS ========================================

# Read From Sensors
# Here we pull the data from the sensors
def ReadFromSensors():
     
     print("-- pulling data from sensors.")
     temperature = pullTempReading()
 
     return temperature
 
#  ==== Tempearture Reading ===6
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def pullTempReading():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = ((temp_c * 9) / 5) + 32
        return temp_f
# ===============

# Connect To Sensors

def tempLight(temperature, fermentationTemp):
    
    upperTempThreshold = fermentationTemp + 10
    lowerTempThreshold = fermentationTemp - 10
    
    GPIO.output(RLEDPin, False)
    GPIO.output(GLEDPin, False)
    GPIO.output(BLEDPin, False)
    
    if temperature > upperTempThreshold:
        GPIO.output (RLEDPin, True)
    
    if temperature < upperTempThreshold and temperature > lowerTempThreshold:
        GPIO.output (GLEDPin, True)
    
    if temperature < lowerTempThreshold:
        GPIO.output (BLEDPin, True)

# ==========================================================================

# Write To DataBase
# - Write to a sql database 
# - fields include style, datebrewed, time, temp, o2, co2, ph, 
#   having a herculomitor reading would be rad to
def WriteToDB(connection, rowID, batchNum, beerStyle, brewDate, fermentationTemp):

    temperature = ReadFromSensors()
    tempLight(temperature, fermentationTemp)

    print("- Sucessfully read from sensors.")
    print("- trying to write")

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S") 

    sql =       """
                INSERT INTO FERMENTATION
                (ROWID, BATCH, STYLE, DATEBREWED, TIME, TEMPERATURE) \
                VALUES (?, ?, ?, ?, ?, ?)
                """

    params = (rowID, batchNum, beerStyle, brewDate, currentTime, temperature)
    connection.execute (sql, params)
    connection.commit ()
    
    print("- Written to database")



# Repeat Function -- come up with a better name
# this function is what will be running once everything is started up.
# this will constantly but every 5 minutes it will kick in to write.
# Once it is ran it will sleep for 1 minute and 1 second 
#    so that it does not write 2 times on the same minute
def RepeatFunction(connection, rowID, fermentationTime, batchNum, beerStyle, brewDate, fermentationTemp):
    print("")
    print("Starting data collection") 

    while (rowID <= fermentationTime * 2016): # 2016 is the amount of times 5 minutes occur in a week
        
        if ( datetime.now().minute not in {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}): 
            print("")
            print("waiting until a multiple of 5 before we write: ", datetime.now())
            sleep(60)
        else: 
            print("")
            print("We are up and running")
            WriteToDB(connection, rowID, batchNum, beerStyle, brewDate, fermentationTemp)
            print("Now sleeping")
            sleep(61)
            print("Now going to repeat")
            rowID = rowID + 1

# Testing
# Testing function, this is to see if the data is correctly being inserted into the database
def testing():
    print("Starting the testing section")
    beerStyle = "ale"
    brewDate = "01.23.4567"

    connection = sqlite3.connect('FERMENTATION.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # WriteToDB(connection, beerStyle, brewDate)
    # sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)
    # sleep(60)
    # WriteToDB(connection, beerStyle, brewDate)
    
    cursor = connection.execute("SELECT BATCH, STYLE, DATEBREWED, TIME, TEMPERATURE from FERMENTATION")
    
    for row in cursor:
        print ("ROWID = ",          row[0])
        print ("BATCH = ",          row[1])
        print ("STYLE = ",          row[2])
        print ("DATEBREWED = ",     row[3])
        print ("TIME = ",           row[4])
        print ("TEMPERATURE = ",    row[5])

    connection.close()
    


# Main
# this is the central operator of the entire program
# [x] need to connect to the database then close
# [x] need to run the timing service
# [x] need to pull data correctly
def main():
    print("Howdy, first we are going to set up the data base for you boss.")
    print("One second please.")

    #testing()

    connection = sqlite3.connect('./FERMENTATION.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    a = cursor.fetchall()

    if not a: 
        print("Making table!")

        connection.execute ('''CREATE TABLE FERMENTATION
                (ROWID          INT     PRIMARY KEY NOT NULL,
                BATCH           INT,
                STYLE           STR,
                DATEBREWED      STR,
                TIME            TIME,
                TEMPERATURE     INT);''')

    print("Connected to database correctly.")

    print("Please write your inputs within qoutes. Working on a way to fix that thank you.")
    batchNum = input("Please enter the batch number of this beer: ")
    batchNum = int(batchNum)
    tempVal = input("Please enter the style of your beer: ") 
    beerStyle = str(tempVal)
    brewDate  = input("Please enter date of brew in the format of --.--.---- ")
    fermentationTemp = input("Please enter your ideal fermentation temperature.")
    fermentationTemp = int(fermentationTemp)
    print("The bounds will be + - 10 *F.")
    fermentationTime = input("Please enter for how long you want to monitor your fermentation.")
    fermentationTime = int(fermentationTime)

    print("Thank you. Begining study.")
    RepeatFunction(connection, 0, batchNum, fermentationTime, beerStyle, brewDate, fermentationTemp)
    
    connection.close()


if __name__ == '__main__':
    main()
