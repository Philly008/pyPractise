# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:45
# @Author     : Philly
# @File       : 10.py
# @Description: 10 lines: Time, conditions, from..import, for..else
from time import localtime
activities = {8: 'Sleeping',
              9: 'commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}
time_now = localtime()
hour = time_now.tm_hour
for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')

