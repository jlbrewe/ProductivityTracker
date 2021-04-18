"""
blueprint from project by Kalle Hallden
https://github.com/KalleHallden/AutoTimer
"""

from __future__ import print_function
import time
from os import system
from activity import *
import json
import datetime
import sys
from pynput.keyboard import Key, Listener
from pynput import keyboard
import logging
import os
import threading
from pynput import mouse

#add new varaibles
keystrokes = 0
clicks = 0


if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    import uiautomation as auto
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from AppKit import NSWorkspace
    from Foundation import *
elif sys.platform in ['linux', 'linux2']:
        import linux as l

active_window_name = ""
activity_name = ""
start_time = datetime.datetime.now()
activeList = AcitivyList([])
first_time = True

time_dict = {}


def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]


def get_active_window():
    _active_window_name = None
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        _active_window_name = win32gui.GetWindowText(window)
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        _active_window_name = (NSWorkspace.sharedWorkspace()
                               .activeApplication()['NSApplicationName'])
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name


def get_chrome_url():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        chromeControl = auto.ControlFromHandle(window)
        edit = chromeControl.EditControl()
        return 'https://' + edit.GetValuePattern().Value
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
        s = NSAppleScript.initWithSource_(
            NSAppleScript.alloc(), textOfMyScript)
        results, err = s.executeAndReturnError_(None)
        return results.stringValue()
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name

def main():

    #added global variables
    global active_window_name
    global first_time
    global start_time
    global keystrokes
    global clicks

    try:
        while True:


            previous_site = ""
            if sys.platform not in ['linux', 'linux2']:
                new_window_name = get_active_window()
                if 'Google Chrome' in new_window_name:
                    new_window_name = url_to_name(get_chrome_url())
            if sys.platform in ['linux', 'linux2']:
                new_window_name = l.get_active_window_x()
                if 'Google Chrome' in new_window_name:
                    new_window_name = l.get_chrome_url_x()


            #changed to form a new entry in JSON every time

            if active_window_name != new_window_name:

                print(active_window_name)
                activity_name = active_window_name

                if not first_time:
                    end_time = datetime.datetime.now()
                    time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
                    time_entry._get_specific_times()


                    exists = False


                    if not exists:
                        #print new message to terminal window
                        print("num of keystrokes: " + str(keystrokes))
                        print("num of clicks: " + str(clicks))
                        #adding a comment in the program thats running
                        activity = Activity(activity_name, [time_entry], keystrokes, int(clicks/2))
                        activeList.activities.append(activity)
                        #resetting the clicks and keystrokes based of window switching
                        clicks = 0
                        keystrokes = 0
                        
                    #do not sort the keys
                    with open('activities.json', 'w') as json_file:
                        json.dump(activeList.serialize(), json_file,
                                indent=4, sort_keys=False)
                        start_time = datetime.datetime.now()
                first_time = False
                active_window_name = new_window_name


            time.sleep(1)
    except KeyboardInterrupt:

        with open('activties.json', 'w') as json_file:
            json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)

#add key press and mouse click capabilities
def on_press(key):
    global keystrokes

    try:
        keystrokes = keystrokes + 1

    except AttributeError:

        keystrokes = keystrokes + 1


def mouse_clicks():

    with mouse.Listener(
        on_click=on_click) as listener:
        listener.join()


def on_click(x, y, button, pressed):
    global clicks
    print(clicks)
    clicks = clicks + 1

#added different threads to keep track of mouslicks and key presses at the same time
def thread_start():

    thread2 = threading.Thread(target=main, args=())
    thread2.start()
    thread3 = threading.Thread(target=mouse_clicks, args=())
    thread3.start()

    with Listener(on_press=on_press) as listener:
        listener.join()

thread_start()
