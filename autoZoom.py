import csv
import webbrowser
import time
import os
import keyboard

file = open('scheduled.csv', 'r')
readed = csv.reader(file, delimiter=',')
scheduled = []
for row in readed:
    if len(row) > 0:
        scheduled.append(row)

file.close()
isStarted = False
for i in range(1, len(scheduled)):
    print("Next Schedule:", scheduled[i][0], "at", scheduled[i][1])
    while True:
        if isStarted == False:
            hour = int(time.strftime("%H"))
            minute = int(time.strftime("%M"))
            start_hour = int(scheduled[i][1].split(':')[0])
            start_minute = int(scheduled[i][1].split(':')[1])
            if hour == start_hour and minute == start_minute - 10: # 10 minutes before class
                isStarted = True

        if isStarted == True:
            webbrowser.open(scheduled[i][8])
            end_hour = int(scheduled[i][2].split(':')[0])
            end_minute = int(scheduled[i][2].split(':')[1])
            start_hour = int(scheduled[i][1].split(':')[0])
            start_minute = int(scheduled[i][1].split(':')[1])
            end_hour *= 3600
            end_minute *= 60
            start_hour *= 3600
            start_minute *= 60
            duration = ((end_hour + end_minute) - (start_hour + start_minute) - 300)
            print('class started')
            time.sleep(duration)
            isStarted = False
            break