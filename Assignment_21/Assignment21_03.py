# Design a Python application where multiple threads update a shared variable.
# • Use a Lock to avoid race conditions.
# • Each thread should increment the shared counter multiple times.
# • Display the final value of the counter after all threads complete execution.

import threading

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt

    for _ in range(2000000):
        with lobj:
            iCnt = iCnt + 1

def main():
    global iCnt

    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)
    t3 = threading.Thread(target=Update)


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Value of iCnt is : ",iCnt)

if __name__ == "__main__":
    main()