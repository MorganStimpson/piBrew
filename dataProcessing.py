# Morgan Stimpson (morgan.stimpson@Hotmail.com)
# piBrew - data processing
# The intention of this pieces is to process the data that occurs from running the raspbery pi

# to call other functions from a different file 
#import piBrew
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import numpy as np

# Scatter Plot

# Boxplot

# Count Outliers
# 
def countOutliers(perfect, low, high):
    conn = sqlite3.connect('FERMENTATION.db')
    sql = "SELECT TEMPERATURE FROM FERMENTATION "
    counter = 0

    df = pd.read_sql(sql, conn)

    for index, row in df.iterrows():
        #print(row[0])
        if(row[0] > low and row[0] < high):
            counter = counter + 1

    conn.close()
    print("There were this many readings within bounds: ", counter)
    # print("There were this many readings out of bounds, ", (df.count() - counter))


# Line Graph
# I have it print the temperature data
# I want to also print a single line of a different color to represent the perfect heat value
# I want a blue line for too cold
# I want a red line for too hot
def lineGraph(perfect, low, high):
    print("Starting the line graph for you boss")

    conn = sqlite3.connect('FERMENTATION.db')
    sql = "SELECT TEMPERATURE FROM FERMENTATION "

    df = pd.read_sql(sql, conn)

    # print(df.head())
    # print(df.tail())

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
    print("What type of graph would you like to see?")
    print("Which elements would you like to observe? Time, Temp, O2, CO2, PH")

    perfect = input("What is the optimal temperature for your beer? ")
    perfect = int(perfect)

    countOutliers(perfect, perfect - 5, perfect + 5)
    lineGraph(perfect, perfect - 5, perfect + 5)



if __name__ == '__main__':
    main()
