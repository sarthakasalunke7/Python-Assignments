# Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
#   ◦ Extract all even elements from the list.
#   ◦ Calculate and display their sum.
# • The OddList thread should:
#   ◦ Extract all odd elements from the list.
#   ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def EvenList(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if(Arr[i] % 2 == 0):
            Sum = Sum + Arr[i]
    
    print(Sum)

def OddList(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if(Arr[i] % 2 != 0):
            Sum = Sum + Arr[i]
    
    print(Sum)

def main():
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        data.append(Value)

    t1 = threading.Thread(target=EvenList,args=(data,))
    t2 = threading.Thread(target=OddList,args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Both threads have finished execution")

if __name__ == "__main__":
    main()