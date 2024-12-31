#!/home/ubuntu/.opentel/bin/python

import time

def snooze(mytime):
    print("+Sleeping for: ", mytime)
    time.sleep(mytime)

if __name__ == "__main__":
    print("========================================")
    snooze(10)
   