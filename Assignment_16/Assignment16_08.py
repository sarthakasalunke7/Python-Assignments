# Write a program which accept number from user and print that number of “*” on screen.
# Input : 5      Output : * * * * *

def NumCheck(No):
    for i in range(No):
        print("*",end=' ')      # Prints * but does NOT move to a new line.Instead, it prints a space after *

def main():
    Value = int(input("Enter a number : "))

    NumCheck(Value)
    
if __name__ == "__main__":
    main() 