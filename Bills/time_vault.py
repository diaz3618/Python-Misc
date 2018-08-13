from datetime import datetime
from crontab import CronTab
import time
RATE = 11.60
PPM = RATE / 60

def main():
    time_controller(0)
    line = "{:5} {:>5} {:<0}"
    work_hrs = float(input("Work hours: "))
    mins = float(time_vault(work_hrs * 60))
    print(mins)

    print(line.format("\n\nWorked:", str(work_hrs), "hrs"))
    print(line.format("Wallet:", "$", str(round(PPM * mins, 3))))


def time_controller(mins):
    cron = CronTab(user=True)
    job  = cron.new(time_vault(mins))
    job.minute.during(5,50).every(5)
    job.hour.every(4)
    job.day.on(4, 5, 6)

    job.dow.on('SUN')
    job.dow.on('SUN', 'FRI')
    job.month.during('APR', 'NOV')

    
    now = datetime.now().strftime('%I:%M:%S %p')
    shift_start = datetime.strptime("09:15:00 PM", "%I:%M:%S %p")
    print(now)
    print(shift_start)
    while str(now) != '09:14:00 PM':
        #print("Waiting...")

        if str(now) == '09:14:00 PM':
            print("Time is now: " + str(now))
            break


def time_vault(_max):
    secs = 0
    mins = 59
    hrs = 0
    time_vault = 59
    wallet = 0
    slp_time = 0.000005

    while time_vault != _max:
        print(str(hrs) + ":" + str(mins) + ":" + str(secs))
        time.sleep(slp_time)
        secs += 1

        if secs == 60:
            mins += 1
            time_vault += 1
            secs = 0
            #print("\t\t" + str(time_vault))
        if mins == 60:
            hrs += 1
            mins = 0
        """
        ## For testing
        if time_vault == _max:
            print("\n\nYou worked " + str(time_vault / 60) + " hours")
            print("Wallet: $" + str(PPM * time_vault))
            print(PPM)
            break
        """
        #print("\n\tDONE!" + str(time_vault))
        if time_vault == _max*60:
            return time_vault


if __name__ == "__main__":
    main()
