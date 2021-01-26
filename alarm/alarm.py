from PIL import Image
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
        p = Image.open("cartoon-alarm-clock-ringing-vector-23354608.jpg")
        p.show()
        playsound("zvonok_starogo_budilnika.mp3")
        playsound("zvonok_starogo_budilnika.mp3")
        snooze=(input("set snooze yes or no"))
        while 1==1:
            if snooze=='yes':
                tsnooze=int(input("enter mitute for snooze"))
                alarmminute+=tsnooze
                break
            else:
                exit()
