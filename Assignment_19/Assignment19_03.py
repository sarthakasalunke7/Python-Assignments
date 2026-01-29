# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

# def FilterMember(No):
#    if(No>=70 and No<=90):
#        return True

# def MapMember(No):
#    return No+10

# def ReduceMember(No1,No2):
#    return No1*No2

def main():
    Value = 0
    data = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for Value in range(Size):
        Value = int(input())
        data.append(Value)

    FData = list(filter(lambda No: 70<=No<=90, data))
    print("List after filter : ",FData)

    MData = list(map(lambda No: No+10, FData))
    print("List after map : ",MData)

    RData = reduce(lambda No1,No2: No1*No2, MData)
    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()