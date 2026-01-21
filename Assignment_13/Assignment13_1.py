# Write a program which accepts length and width of rectangle and prints area.

def RectArea(l, b):
    return l*b

def main():
    Area = 0

    Length = int(input("Enter length of rectangle : "))
    Breadth = int(input("Enter breadth of rectangle : "))

    Area = RectArea(Length, Breadth)

    print("Area of rectangle : ",Area)

if __name__ == "__main__":
    main()