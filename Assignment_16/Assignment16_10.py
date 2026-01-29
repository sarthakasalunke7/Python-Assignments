# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous     Output : 10

def DisplayLength(A):
    return len(A)

def main():
    Ret = 0

    String = input("Enter a string : ")

    Ret = DisplayLength(String)

    print(Ret)
    
if __name__ == "__main__":
    main() 