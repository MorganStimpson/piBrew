# Morgan Stimpson (morgan.stimpson@hotmail.com)
# 
# piBrew
# This is intended to study and monitor the fermentation rate of beer currently brewing.

#import section
from datetime import datetime
from time import sleep, time

# Connect To Server
# this will make an attempt to connect to a sql server that is running on the localhost
# connect to the server
# is there a db? 
# if not make one
def connectToServer():
    print("foo")

    if(1 == 2):
        return 1
    return 0


# ReadFromSensors
def readFromSensors():
    print("-- connecting to sensors.")

# WriteToDB
# Write to a sql database 
# fields include time, temp, o2, co2, ph, having a herculomitor reading would be rad to
def WriteToDB():

    readFromSensors()

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S") 

    print("- trying to write")
    print("- Current Time =", currentTime)
    print("- written")


# Repeat Function -- come up with a better name
# this function is what will be running once everything is started up.
# this will constantly but every 15 minutes it will kick in to write.
def repeatFunction():

    condition = False

    while datetime.now().minute not in {0, 15, 30, 45}: 
        print("waiting 15 minutes before we write")
        sleep(60) # this is in seconds, it will attempt to write every 1 minutes.
    
    def timer():
        print("We are up and running")
        WriteToDB()
        # this is necessary since it will run in a near infinite loop and will crash. --stackoverflow
        sleep(60) 
        main()

    timer()



# Main
# this is the central operator of the entire function
# [] need to connect to the server to post the data
# [] need to run the timing service
def main():
    print("howdy, first we are going to set up the server to host data.")
    print("one second please.")
    
    connectToServer()
    print("connected to server")
    print("starting data collection")

    repeatFunction()


if __name__ == '__main__':
    main()
