# Write a program which accepts one number and prints multiplication table of that number
# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40

def Multi(Value):
    data = list()

    for i in range(1,11):
        mult = i*Value
        data.append(mult)

    return data

def main():
    print("Enter a number : ")
    No = int(input())

    table = []

    table = Multi(No)

    print(*table)       # * is unpacking operator , *table unpacks the list elements , Default separator is a space



if __name__ == "__main__":
    main()