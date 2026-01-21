# Write a program which accepts radius of circle and prints area of circle.

def CircleArea(r):
    PI = 3.14
    return PI*r*r  # PI*r**2

def main():
    Area = 0

    Radius = int(input("Enter radius of a circle : "))

    Area = CircleArea(Radius)

    print("Area of circle : ",Area)

if __name__ == "__main__":
    main()