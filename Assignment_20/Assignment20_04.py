# Design a Python application that creates three threads named Small, Capital, and Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
#   ◦ Thread ID
#   ◦ Thread Name

import threading

def Small(Str):
    Count = 0

    print("Thread id is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)

    for ch in Str:
        if(ch.islower()):
            Count = Count + 1

    print("Lowercase count:", Count)

def Capital(Str):
    Count = 0

    print("Thread id is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)

    for ch in Str:
        if(ch.isupper()):
            Count = Count + 1

    print("Uppercase count:", Count)

def Digits(Str):
    Count = 0

    print("Thread id is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread().name)

    for ch in Str:
        if(ch.isdigit()):
            Count = Count + 1

    print("Digit count:", Count)

def main():

    string = input("Enter a string: ")

    t1 = threading.Thread(target=Small,args=(string,))
    t2 = threading.Thread(target=Capital,args=(string,))
    t3 = threading.Thread(target=Digits,args=(string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Both threads have finished execution")

if __name__ == "__main__":
    main()