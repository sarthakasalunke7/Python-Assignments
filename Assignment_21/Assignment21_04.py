# Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.

import threading

Sum = 0
Mult = 1

def Thread1(Arr):
    global Sum

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

def Thread2(Arr):
    global Mult

    for i in range(len(Arr)):
        Mult = Mult * Arr[i]

def main():
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        data.append(Value)

    t1 = threading.Thread(target=Thread1, args=(data,))
    t2 = threading.Thread(target=Thread2, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements : ",Sum)
    print("Product of elements : ",Mult)

if __name__ == "__main__":
    main()