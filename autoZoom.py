from csv import reader, writer
import webbrowser
from time import strftime, sleep
from os import system
from datetime import timedelta

def changeFormat(date: str):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day, month, year = date.split('/')
    month = months[int(month) - 1]
    return f'{day} {month} {year}'

file = open('schedule.csv', 'r')
readed = reader(file, delimiter=',')
schedule = []
for row in readed:
    if len(row) > 0:
        schedule.append(row)

file.close()

today = strftime("%d/%m/%Y")
today = changeFormat(today)

isStarted = False
for i in range(1, len(schedule)):
    print("Next Schedule:", schedule[i][0], "at", schedule[i][1])
    print("Class Name: {} - {}".format(schedule[i][4], schedule[i][5]))
    while True:
        if isStarted == False:
            hour = int(strftime("%H"))
            minute = int(strftime("%M"))
            start_hour = int(schedule[i][1].split(':')[0])
            start_minute = int(schedule[i][1].split(':')[1])
            start_date = schedule[i][0]
            if hour >= start_hour and minute >= start_minute - 10 and today == start_date: # 10 minutes before class
                isStarted = True

            if hour >= 24:
                today = changeFormat(strftime("%d/%m/%Y"))

        if isStarted == True:
            webbrowser.open(schedule[i][8])
            end_hour = int(schedule[i][2].split(':')[0])
            end_minute = int(schedule[i][2].split(':')[1])
            start_hour = int(schedule[i][1].split(':')[0])
            start_minute = int(schedule[i][1].split(':')[1])
            end_hour *= 3600
            end_minute *= 60
            start_hour *= 3600
            start_minute *= 60
            duration = ((end_hour + end_minute) - (start_hour + start_minute) - 300)
            print('Class Started')
            lines = list()
            with open('schedule.csv', 'r') as f:
                reader = reader(f)
                for row in reader:
                    lines.append(row)

            with open('schedule.csv', 'w') as f:
                writer = writer(f)
                for row in lines:
                    if len(row) > 0:
                        if row[0] != schedule[i][0] and row[1] != schedule[i][1]:
                            writer.writerow(row)

            while duration > 0:
                print('Time Left:', timedelta(seconds=duration))
                sleep(1)
                duration -= 1
                system('cls')
            isStarted = False
            break