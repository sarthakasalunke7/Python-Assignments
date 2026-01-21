# Write a program which accepts marks and displays grade.
# Condition Example:
# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail

def Display(No):
    if(0 > No or No > 100):     # Invalid marks
        return -1
    elif(No < 50):              # Fail
        return 1
    elif(50 <= No < 60):        # Second Class
        return 2
    elif(60 <= No < 75):        # First Class
        return 3
    elif(No >= 75):             # Distinction
        return 4

def main():
    Ret = 0 

    Marks = int(input("Enter Marks : "))

    Ret = Display(Marks)

    if(Ret == -1):
        print("Invalid Marks")
    elif(Ret == 1):
        print("Fail")
    elif(Ret == 2):
        print("Second Class")
    elif(Ret == 3):
        print("First Class")
    elif(Ret == 4):
        print("Distinction")

if __name__ == "__main__":
    main()