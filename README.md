# piBrew

**Developed by [Morgan Stimpson](mailto:morgan.stimpson@hotmail.com)**

Using a Raspberry Pi to study the fermentation rate of wort or other fermentable liquids.

## Usage

### Requirements

* Raspberry Pi with the following installed:
  * Tmux
  * SQLite3
  * Python3
  * Matplotlib
  * ?

### Running the script

1. Boot your Raspberry Pi (do you need to ensure any GPIO is hooked up? if yes, mention that before boot?)
2. Start a tmux session
   1. Directly from the pi start a new tmux session from terminal, or
   2. Alternatively, ssh from another computer using tmux
3. CD to where the program sits
4. Start the script
5. Detach from the TMUX session with `ctrl-b d`
6. Answer the initial start up state with `"<your answer in quotes>"` (do not include the angled brackets `<>`)
7. Reattach the tmux session with `tmux a`
8. `ctrl-c` the program data should be stored

## Data Processing

1. Line Graph -- to show data over time
2. // Starting to think about other methods to develop

## Goal:

This indicates it has been completed

1. -Produce 1 model-
2. -Equip a fermentation tank with sensors-
3. -Let wort ferment into beer.-
4. -Constantly pull data and store in a SQLite3 database-
5. -Train on the model to create a generic model.-
6. -Use the data to predict for the next batch or future batches-
7. Adjust bounds of lighting alg.
8. Figure out how to not need to make a new db but only a table
9. Figure out how to get the last rowID if the pi crashes and needs to restart
10. Use the last rowId to continue the fermentation db
11. Create a server to host data
12. Graph data on the server 

## Technologies Used:

* Python      - Programming Language to conduct everything within
* SQLite3     - Database
* MathPlotLib - Data viewing
* Rasbian     - OS of the Raspbery Pi
* TMUX        - Run a terminal, start the program, allow for the client to leave the pi and let it run.

## Equipment List:

1. Raspberry Pi 4B:
   * CanaKit Raspberry Pi 4 Starter Kit
   * 32 GB EVO+
   * Case w/ fan
   * 8gb Ram
   * Link;
2. Breadboard:
   * Full size recommended
   * Link;
3. Wiring:
   * Male to male wriring
   * Female to Female wiring
   * Male to Female wiring
   * Resistors
4. Lights:
   * 1x Red Light;      Hot Indicator
   * 1x Green Light;    Ideal indicator
   * 1x Blue Light;     Cold indicator
5. Sensors:
   * *Temperature Sensor*
   * Model: DS188B20 Temperature Sensor
   * Purpose: To follow the the temperature change of the fermenting wort. The temperatur change affects all following sensors and the data that they will pull from their readings.
   * *O2 Sensor*
   * Model:
   * Purpose:
   * Once most of the O2 is gone the yeast stops reproducing and begins the bulk of the fermentation
   * *PH Sensor*
   * Model:
   * Purpose:
   * The acidity of the liquid will kill of the yeast and prevent further fermentation
   * Others // I can not remember at the moment

## Resources:

1. Raspberry Pi Headless set up;
   * https://www.youtube.com/watch?v=dhY8m_Eg5iU&t=107s
3. Temperature Reading;
   * https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
5. PH Reading;
   * https://myhydropi.com/connecting-a-ph-sensor-to-a-raspberry-pi
