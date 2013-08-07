import third_party_libs
from model.json_property import JsonProperty
from util import TimeRange, clock
from itertools import imap
from functools import partial
from datetime import time
# from flufl import enum

# WeekDays =  enum.make("WeekDays", [("Mon", 0), ("Tue", 1), ("Wed", 2),
#                                    ("Thu", 3), ("Fri", 4), ("Sat", 5), ("Sun", 6)])

# class WeekHoursProperty(JsonProperty):
#     def to_json(self, result):
#         return (result).json() if result else None
#     def make_value_from_datastore(self,  value):
#         json = super(WeekHoursProperty,  self).make_value_from_datastore(value)
#         return WeekHours.from_json(json)


# def time_ranges_str(time_ranges):
#     return ','.join(map(str, time_ranges))

# class WeekHours(object):
#     def __init__(self):
#         self._weekhours = [[], [], [], [], [], [], []] 

#     def add_hours(self, weekday, start, end):
#         self.add_time_range(weekday, TimeRange(start, end))
#         return self
        
#     def add_time_range(self, weekday, time_range):
#         if not time_range in self[weekday]:
#             self[weekday].append(time_range)
#         return self
        
#     def add_time_ranges_str(self, time_ranges_strs):
#         for i, time_ranges_str in enumerate(time_ranges_strs):
#             self.add_time_range_str(i, time_ranges_str)
#         return self
        
#     def add_time_range_str(self, weekday, time_ranges_str):
#         if not time_ranges_str:
#             return
#         for time_range_str in time_ranges_str.split(','):
#             self.add_time_range(weekday,
#                                 TimeRange(*clock.time_from_string(
#                                     *time_range_str.split("-"))))
#         return self

#     def is_datetime_in_range(self, datetime):
#         return self.is_in_range(datetime.weekday(), datetime.time())
        
#     def is_in_range(self, weekday, hour):
#         in_range = partial(TimeRange.is_in_range, value = hour)
#         return any(imap(in_range, self[weekday]))

#     def __getitem__(self, day):
#         return self._weekhours[int(day)]

#     @property
#     def time_ranges_strs(self):
#         return [(weekday.name, time_ranges_str(self[int(weekday)]))
#                 for weekday in WeekDays]

#     @staticmethod
#     def make_24_x_7():
#         week_hours = WeekHours()
#         for day in WeekDays:
#             week_hours.add_time_range(int(day), TimeRange.hours_24())
#         return week_hours
        
#     def time_ranges_str(self, time_ranges):
#         return ", ".join([time_range.strftime("%I:%M %p")
#                           for time_range in time_ranges])

#     def str_rep(self):
#         buckets = [([0], self[0])]
#         for i in range(1, 7):
#             if self[i] == buckets[-1][1]:
#                 buckets[-1][0].append(i)
#             else:
#                 buckets.append(([i], self[i]))
#         if len(buckets) == 1:
#             return [self.time_ranges_str(buckets[0][1])]
#         strs = []
#         for days, time_ranges in buckets:
#             times_str = self.time_ranges_str(time_ranges)
#             if len(days) > 2:
#                 strs.append("%s - %s : %s" %  (WeekDays[days[0]].name,
#                                                WeekDays[days[-1]].name,
#                                                times_str))
#             else:
#                 strs.append("%s : %s" % (", ".join(WeekDays[i].name for i in days),
#                                      times_str))
#         return strs

#     def __str__(self):
#         return "\n".join(self.str_rep())

#     @staticmethod
#     def from_json(json):
#         if not json:
#             return None
#         assert len(json) == 7
#         weekhours = WeekHours()
#         for day, time_ranges in enumerate(json):
#             for time_range in time_ranges:
#                 weekhours.add_hours(day, 
#                     time(time_range[0][0], time_range[0][1]),
#                     time(time_range[1][0], time_range[1][1]))
#         return weekhours

#     def __iter__(self):
#         return enumerate(self._weekhours)

#     def json(self):
#         return [[[[time_range.start.hour, time_range.start.minute],
#                   [time_range.end.hour, time_range.end.minute]
#                   ] for time_range in dayhours] for dayhours in self._weekhours]
#     def __eq__(self, other):
#         return self._weekhours == other._weekhours

