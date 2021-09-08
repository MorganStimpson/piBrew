# Morgan Stimpson (morgan.stimpson@Hotmail.com)
# piBrew - data processing
# The intention of this pieces is to process the data that occurs from running the raspbery pi
#  and it's extras

# I do not know of other graphs that would help

# to call other functions from a different file 
#import piBrew
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
import numpy as np
from pprint import pprint

# Scatter Plot

# Boxplot

# Line Graph
# work on this
def lineGraph():
    print("Starting the line graph")

    conn = sqlite3.connect('FERMENTATION.db')
    sql = "SELECT TEMPERATURE FROM FERMENTATION "

    df = pd.read_sql(sql, conn)
    
    print(df.head())
    print(df.tail())

    plt.plot(df)
    plt.show()
    


# Main
def main():
    print("Starting data processing")
    print("What type of graph would you like to see?")
    print("Which elements would you like to observe? Time, Temp, O2, CO2, PH")

    lineGraph()

    # connect to db
    connection = sqlite3.connect('FERMENTATION.db') # this will make a db if none are found -- if there is one skip
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # disconnect from db
    connection.close() # don't forget to close the db when you're finsihed



if __name__ == '__main__':
    main()
