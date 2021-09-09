# Morgan Stimpson (morgan.stimpson@Hotmail.com)
# piBrew - data processing
# The intention of this pieces is to process the data that occurs from running the raspbery pi

# to call other functions from a different file 
#import piBrew
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import numpy as np

# Count Outliers
# This function counts the outliers of the data
# This function prints out values to help the brewer get a sense of their fermentation
#  process.
def countOutliers(perfect, low, high):
    conn = sqlite3.connect('FERMENTATION.db')
    sql = "SELECT TEMPERATURE FROM FERMENTATION "
    
    aboveInBounds    = 0
    belowInBounds    = 0
    aboveOutOfBounds = 0
    belowOutOfBounds = 0

    df = pd.read_sql(sql, conn)
    conn.close()

    for index, row in df.iterrows():
        if(row[0] <= high and row[0] >= perfect):
            aboveInBounds = aboveInBounds + 1
        if(row[0] <= perfect and row[0] >= low):
            belowInBounds = belowInBounds + 1
        if(row[0] > high):
            aboveOutOfBounds = aboveOutOfBounds + 1
        if(row[0] < low):
            belowOutOfBounds = belowOutOfBounds + 1

    print("This is the percentage spent in the bounds, ", ((aboveInBounds + belowInBounds) / df.size ) * 100,"% ")

    if(aboveInBounds + belowInBounds > aboveOutOfBounds + belowOutOfBounds):
        if(aboveInBounds > belowInBounds):
            print("The fermentation sat on the warmer side of the bounds")
            print("This is the percentage spent in the warmer bounds, ", (aboveInBounds/ df.size ) * 100,"% ")
        else:
            print("The fermentation sat around the colder side of the bounds")
            print("This is the percentage spent in the colder bounds, ", (belowInBounds/ df.size ) * 100,"% ")
    else:
        print("Your fermentation sat outside of the goal range for the majority of the time")
        print("This is the percentage spent in the warmer bounds, ", ((belowOutOfBounds + aboveOutOfBounds)/ df.size ) * 100,"% ")
        if(aboveOutOfBounds > belowOutOfBounds):
            print("The fermentation process was warm for the majority of the time")
        else:
            print("The fermentation was cold for the majority of the time")

# Line Graph (temperatrue v time)
# This function takes in the ideal temp and it's buffers.
# This function then pulls the fermentation.db data
# This function returns a graph to represent the fermentation process.
# There is a green lien for perfect temperature
# There is a blue line for too cold
# There is a red line for too hot
def lineGraph(perfect, low, high):
    print("Starting the line graph for you boss")

    conn = sqlite3.connect('FERMENTATION.db')
    sql = "SELECT TEMPERATURE FROM FERMENTATION "

    df = pd.read_sql(sql, conn)

    plt.plot(df, 'm')
    plt.axhline(y=perfect, color='g')
    plt.axhline(y=low, color='b')
    plt.axhline(y=high, color='r')

    plt.title("Temperature over Time")
    plt.xlabel("Time in multiples of 5")
    plt.ylabel("Temperature (*F)")
    
    plt.show()
    conn.close()


# Main
def main():
    print("Starting data processing")

    perfect = input("What is the optimal temperature for your beer? ")
    bound   = input("How far are the bounds that you would like (most common is 5 to 10)? ")
    perfect = int(perfect)
    bound   = int(bound)

    countOutliers(perfect, perfect - bound, perfect + bound)
    lineGraph(perfect, perfect - bound, perfect + bound)



if __name__ == '__main__':
    main()
