# Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

import threading

def Thread1(Arr):
    Max = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] > Max):
            Max = Arr[i]

    print("Maximum element : ",Max)

def Thread2(Arr):
    Min = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    print("Minimum element : ",Min)

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

if __name__ == "__main__":
    main()