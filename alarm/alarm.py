import datetime
from playsound import playsound


alarmhour=int(input("enter the hour do you want to wakeup"))
alarmminute=int(input("enter the minute do you want wakeup"))
ampm=str(input("enter am or pm :"))
if ampm=="pm":
    alarmhour=alarmhour+12

while 1==1:
    if alarmhour==datetime.datetime.now().hour and alarmminute==datetime.datetime.now().minute:
        print("wakeup wakwup....")
        playsound("zvonok_starogo_budilnika.mp3")
        playsound("zvonok_starogo_budilnika.mp3")
        break
