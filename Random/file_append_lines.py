import multiprocessing
import random
import time


def appendNumbers():
    for i in range(50000000):
        number = random.randrange(50)
        time.sleep(1)
        with open('filelines.txt', 'a') as f:
            f.write(str(number)+"\n")


def main():
    while True:
        p = multiprocessing.Process(target=appendNumbers, name="appendNumbers", args=())
        p.start()

        time.sleep(10)

        p.terminate()

        p.join()

        print "Round Done"
        print "Wait Starts"
        time.sleep(5)
        print "Wait Ends"


main()
