# Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

import threading

def isPrime(No):
    if(No <= 1):
        return False
    
    for i in range(2,int(No/2)+1):
        if(No % i == 0):
            return False
        
    return True

def Prime(Arr):
    print("Prime Numbers : ")

    for i in range(len(Arr)):
        if(isPrime(Arr[i]) == True):
            print(Arr[i],end=" ")

def NonPrime(Arr):
    print("Non Prime Numbers : ")

    for i in range(len(Arr)):
        if(isPrime(Arr[i]) == False):
            print(Arr[i],end=" ")

def main():
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        data.append(Value)

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()