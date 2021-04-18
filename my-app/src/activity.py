"""
blueprint from project by Kalle Hallden
https://github.com/KalleHallden/AutoTimer
"""

#added keystrokes and mouse click variables
#changed capitalization

import datetime
import json
from dateutil import parser


class AcitivyList:
    def __init__(self, activities):
        self.activities = activities

    def initialize_me(self):
        activity_list = AcitivyList([])
        with open('activities.json', 'r') as f:
            data = json.load(f)
            activity_list = AcitivyList(
                activities = self.get_activities_from_json(data)
            )
        return activity_list

    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name = activity['Name'],
                    keystrokes = activity['Keystrokes'],
                    clicks = activity['Clicks'],
                    time_entries = self.get_time_entires_from_json(activity)
                )
            )


        self.activities = return_list
        return return_list

    def get_time_entires_from_json(self, data):
        return_list = []
        for entry in data['Time']:
            return_list.append(
                TimeEntry(
                    start_time = parser.parse(entry['Start Time']),
                    end_time = parser.parse(entry['End Time']),
                    days = entry['Days'],
                    hours = entry['Hours'],
                    minutes = entry['Minutes'],
                    seconds = entry['Seconds'],
                )
            )
        self.time_entries = return_list
        return return_list

    def serialize(self):
        return {
            'activities' : self.activities_to_json()
        }

    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())

        return activities_


class Activity:
    def __init__(self, name, time_entries, keystrokes, clicks):
        self.name = name
        self.keystrokes = keystrokes
        self.clicks = clicks
        self.time_entries = time_entries

    def serialize(self):
        return {
            'Name' : self.name,
            'Keystrokes' : self.keystrokes,
            'Clicks' : self.clicks,
            'Time' : self.make_time_entires_to_json()
        }

    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list


class TimeEntry:
    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def _get_specific_times(self):
        self.days, self.seconds = self.total_time.days, self.total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

    def serialize(self):
        return {
            'Start Time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'End Time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'Days' : self.days,
            'Hours' : self.hours,
            'Minutes' : self.minutes,
            'Seconds' : self.seconds
        }
