# Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#           * * * *
#            * * *
#             * *
#              *

def Display(No):
    for i in range(No, 0, -1):
        for space in range(No - i):
            print(" ", end="")
        for star in range(i):
            print("* ", end="")
        
        print()

def main():
    Value = int(input("Enter a number : "))
    Display(Value)

if __name__ == "__main__":
    main()