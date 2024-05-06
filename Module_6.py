import multiprocessing
import time
import datetime 
import random

#13.1
file = open("today.txt", "w") 
file.write(time.ctime(time.time()))
file.close()

#13.2
file = open("today.txt", "r") 
today_string = file.readlines()[0]
file.close()

#13.3
date = datetime.datetime.strptime(today_string, "%a %b %d %X %Y")
print(date)

#15.1
def wait():
    time.sleep(random.random()) #Random returns value between 0-1, wait for that many seconds
    print(datetime.datetime.now())

def main15():
    #create three processes
    a = multiprocessing.Process(target=wait)
    b = multiprocessing.Process(target=wait)
    c = multiprocessing.Process(target=wait)
    #start all processes
    a.start(); b.start(); c.start()
    #terminal all processes after 2 seconds
    time.sleep(2)
    a.terminate(); b.terminate(); c.terminate()

if __name__ == '__main__':
    #main15()
    pass