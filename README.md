# piBrew - developed by Morgan Stimpson
Using a Raspberry Pi to study the fermentation rate of wort or other fermentable liquids.

## How To Run It:
1.  Start up your Raspberry Pi
2.  Have Tmux/SQLite3/? installed on your Raspberry Pi
3.  From a either the Pi or another computer start an ssh TMUX client
4.  CD to where the program sits
5.  Start the program with "python piBrew.py"
6.  Deattach from the TMUX session with ctrl-b d
7.  Let the program run as long as needed
8.  Reattach the tmux session w/ "tmux a"
9.  Ctrl-c the program data should be stored
10. Look at your data

## Data Processing
1. Line Graph
2. BoxPlot
3. Scatter PLot
4. // Starting to think about other methods to develop

## Goal:
1. Produce 1 model
2. Equip a fermentation tank with sensors
3. Let wort ferment into beer.
4. Constantly pull data and store in a SQLite3 database
5. Train on the model to create a generic model.
6. Use the data to predict for the next batch or future batches

## Technologies Used:
Python      - Programming Language to conduct everything within
SQLite3     - Database
MathPlotLib - Data viewing
Pandasd     - Machine Learning / Data Processing
Rasbian     - OS of the Raspbery Pi
TMUX        - Run a terminal, start the program, allow for the client to leave the pi and let it run.

## Equipment List:
1. Raspberry Pi 4B:
    1a. CanaKit Raspberry Pi 4 Starter Kit
        32 GB EVO+
        Case w/ fan
        8gb Ram
        Link;
2. Breadboard:
    Full size recommended
    Link;
3. Wiring:
    ???
4. Sensors:
* *Temperature Sensor*
* Model: DS188B20 Temperature Sensor
* Purpose: To follow the the temperature change of the fermenting wort. The temperatur change affects all following sensors and the data that they will pull from their readings.
* *O2 Sensor* 
* Model:
* Purpose:
* Once most of the O2 is gone the yeast stops reproducing and begins the bulk of the fermentation
* *CO2 Sensor*
* Model:
* Purpose: 
* This will have a relation with the O2, but not sure exactly at the moment
* *Time*
* Model:
* Purpose:
* This piece of information is coming from the clock on board
* *PH Sensor*
* Model:
* Purpose: 
* The acidity of the liquid will kill of the yeast and prevent further fermentation
* Others // I can not remember at the moment

## Resources:
1. Temperature Reading;
    https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
2. PH Reading;
    https://myhydropi.com/connecting-a-ph-sensor-to-a-raspberry-pi
3. Tmux Cheat sheet
    https://tmuxcheatsheet.com/
4. Matplotlib
    
