import requests
from csv import writer
from json import loads
from pandas import read_csv
from getpass import getpass

s = requests.Session()

print('BinusMaya Login')
print('===============')
print('Input username without @binus.ac.id!')
username = input("Username: ")
password = getpass()

data = {
    'Username': username,
    'Password': password
}

s.post('https://myclass.apps.binus.ac.id/Auth/Login', data=data)
print('Getting schedule data...\n')
r = s.get('https://myclass.apps.binus.ac.id/Home/GetViconSchedule')

with open('schedule.json', 'w') as f:
    f.write(r.text)

schedule_data = open('schedule.json', 'r').read()
x = loads(schedule_data)
fullName = x[0]['FullName']

file = open('scheduled.csv', 'w')

f = writer(file)

f.writerow(["DisplayStartDate", "StartTime", "EndTime", "ClassCode", "CourseCode", "CourseTitleEn", "MeetingId", "MeetingPassword", "MeetingUrl"])

for x in x:
    f.writerow([x['DisplayStartDate'], x['StartTime'], x['EndTime'], x['ClassCode'], x['CourseCode'], x['CourseTitleEn'], x['MeetingId'], x['MeetingPassword'], x['MeetingUrl']])

file.close()

schedule = open('scheduled.csv', 'r')
readed = read_csv(schedule)
print('Hello ' + fullName + '!')
print('Your schedule is:' + '\n')
print(readed)
schedule.close()
print('\nYour schedule is saved to scheduled.csv')
print('Have a nice day!')