# piBrew - developed by Morgan Stimpson
Use a Raspberry Pi to study the fermentation rate of wort or other fermentable liquids.

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
2. 
