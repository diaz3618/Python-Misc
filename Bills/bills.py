"""
The program is going to keep running on a pre-set date and time (start and end of shift).
While its running, it counts how many hours the user has worked to be able to pay "x" bill.

Ej.
11.60 x hrs, approx. 45 hrs/2wks
f(x)=522-11.60x ($522 = 45 hrs in 2 weeks)


## Program UI idea:

Today is July 02, 2018.

Bills checked so far:
    [+]Phone bill
    [+]Netflix

Monitoring shifts from 07/02/2018 - 07/28/2018:    (Shift will be saved in a csv file)
slaving to pay the next bill...

[+]Your worked 13 hours!
    [x]GRU bill

slaving to pay the next bill...

[+]Your worked 18 hours!
    [x]GRU bill
    [x]USAA Insurance bill

    $56 left
    Additional expenses(default = 0)
    1: 20
    2: 6
    3: 0 (0 = break loop)
    
    $30 left
    
slaving to pay the next bill...

## Save all the checked bills so they can be printed when the program starts 

"""

import time
import datetime
from threading import Timer
RATE = 11.60
YEAR = datetime.date.today().year
MONTH = datetime.date.today().month
DATE = datetime.date.today()
DAY = datetime.date.today().day

def _day(day):
    day_str = ""
    
    if day <= 9:
        day_str = "0"+str(day)
        print(day_str)
    else:
        print(day)

def main():
    #day()
    print()
    IO()
##    #print(datetime.datetime.now())
##    #_time()
##    x = datetime.today()
##    y = x.replace(day = x.day+1, hour = 1, minute = 0, second = 0, microsecond = 0)
##    print("X: " + str(x))
##    print("Y: " + str(y))
##    delta_t =  y - x
##
##    secs=delta_t.seconds+1
##    print(secs)

##def hello_world():
##    print ("hello world")
##    #...
##
##    t = Timer(secs, hello_world)
##    t.start()

def IO():
    day = int(input("Day: "))
    start = float(input("Start: "))
    end = float(input("End: "))
    
    print("\n\n\n")
    
    print(str(_day(day)))

    print("\n\n\n")
    #shift = 2018-07-26 01:45:02.072340
    if YEAR == 2018:
        print("It works!")
        print("DATE variable: " + str(DATE))
        print("Date with 3 variables: " + str(YEAR) + "-" + str(MONTH) + "-" + str(DAY))

##def _time(day, start, end):
##    x = datetime.today()
##    y = x.replace(day = x.day+1, hour = 1, minute = 0, second = 0, microsecond = 0)
##    print("X: " + str(x))
##    print("Y: " + str(y))
##    delta_t =  y - x
##
##    secs=delta_t.seconds+1
##    print(secs)
##
##def bills():
##    hours = float(input("Hours this week: "))
##
##    work_hrs = RATE * hours
    

if __name__ == "__main__":
    main()
