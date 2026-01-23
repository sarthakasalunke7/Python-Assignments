# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

def main():
    Size = 0
    Value = 0
    data = []

    Size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    FData = list(filter(lambda No : No%2 == 0, data))

    print("Count of even numbers is : ",len(FData))
    
if __name__ == "__main__" : 
    main()