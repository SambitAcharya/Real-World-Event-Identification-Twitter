import multiprocessing
import time

def foo(n):
    for i in range(10000 * n):
        print "Tick"
        time.sleep(1)

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()

    time.sleep(10)

    p.terminate()

    p.join()
