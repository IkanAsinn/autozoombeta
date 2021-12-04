import requests
from csv import writer
from json import loads
from pandas import read_csv
from getpass import getpass
from os import system, remove

s = requests.Session()
url = 'https://myclass.apps.binus.ac.id/'
status = False

while not status:
    print('BinusMaya Login')
    print('===============')
    username = input("Username: ")
    password = getpass()
    if '@' in username:
        username = username.split('@')[0]

    data = {
        'Username': username,
        'Password': password
    }
    r = s.post(url + '/Auth/Login', data=data)
    resp_status = r.json()
    status = resp_status.get('Status')
    if status == True:
        print('Login Success\n')
        break
    else:
        print('Login Failed')
        input('Press enter to try again')
        system('cls')


print('Getting schedule data...\n')
r = s.get(url + '/Home/GetViconSchedule')

with open('schedule.json', 'w') as f:
    f.write(r.text)

schedule_data = open('schedule.json', 'r').read()
x = loads(schedule_data)
fullName = x[0]['FullName']

remove('schedule.json')

file = open('schedule.csv', 'w')

f = writer(file)

f.writerow(["DisplayStartDate", "StartTime", "EndTime", "ClassCode", "CourseCode", "CourseTitleEn", "MeetingId", "MeetingPassword", "MeetingUrl"])

for x in x:
    f.writerow([x['DisplayStartDate'], x['StartTime'], x['EndTime'], x['ClassCode'], x['CourseCode'], x['CourseTitleEn'], x['MeetingId'], x['MeetingPassword'], x['MeetingUrl']])

file.close()

schedule = open('schedule.csv', 'r')
readed = read_csv(schedule)

print('Hello ' + fullName + '!')
print('Your schedule is:' + '\n')
print(readed)

schedule.close()

print('\nYour schedule is saved to schedule.csv')
print('Have a nice day!')