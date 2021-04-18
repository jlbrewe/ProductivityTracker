# ProductivityTracker :computer: :ballot_box_with_check:
ProductivityTracker is a product that tracks user actions and formats into a table that includes window name, number of keystrokes for the window, number of mouse clicks for the window, and the time spent on the window. There is also a countdown capabliity that alerts the user when the time is complete.

## Table of Contents
* [Installation](#installation)
* [How To Run](#how-to-run)
* [Requirements](#requirements)
* [Blueprints](#blueprints)

## Installation

To clone and work on the repository, you can run the command:
```
https://github.com/jlbrewe/ProductivityTracker.git
```
To install node modules, you will need to have Node.js installed and use these commands in the main folder:
```
npm install
npm install react-to-json
npm install fontsource-roboto
npm install @material-ui/core --save
npm install pynput
npm install python-dateutil
npm install react-json-to-table
npm install os
npm install threading
npm install datetime
npm install sys
npm install time
npm install json
npm install subprocess
npm install re
```

## How to Run
1. Navigate to the cloned repo folder and move the node_modules folder into the my-app folder.
2. Open two terminal windows
3. In one terminal window, navigate to /my-app/src and run the command:
```
python3 autotimer.py
```
4. In the other terminal window, navigate to /my-app and run the command:
```
npm start
```
6. When the localhost window pops up, pop it out, making sure it is in its own seperate window (if desired, set the countdown and start).


## Requirements
  
  Requirements:
  * Python 3.8 or higher
  * Node.js (React Frontend)

## Blueprints

  Projects used as blueprints for this project:
  * Countdown Feature: https://github.com/peterdurham/timers-demo
  * Activity Tracking Feature: https://github.com/KalleHallden/AutoTimer
