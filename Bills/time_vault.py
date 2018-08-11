from datetime import *
import time
RATE = 11.60
PPM = RATE / 60

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

def main():
    line = "{:5} {:>5} {:<0}"
    work_hrs = float(input("Work hours: "))
    mins = time_vault(work_hrs * 60)

    print(line.format("\n\nWorked:", str(work_hrs), "hrs"))
    print(line.format("Wallet:", "$", str(round(PPM * mins, 3))))

if __name__ == "__main__":
    main()
