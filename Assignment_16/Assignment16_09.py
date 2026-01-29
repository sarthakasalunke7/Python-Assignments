# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def DisplayEven():
    Count = 0
    Sum = 0
    data = []

    while(Count < 10):
        Sum = Sum + 2
        data.append(Sum)
        Count = Count + 1
    
    return data

def main():
    Ret = []

    Ret = DisplayEven()

    print(*Ret)

if __name__ == "__main__":
    main() 