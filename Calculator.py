import sys

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return x ** y
def findSin(hyp, opp):
    return opp / hyp
def findCos(hyp, adj):
    return adj / hyp
def findTan(adj, opp):
    return opp / adj

def Calculator():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exponent\n6. Find Sin\n7. Find Cos\n8. Find Tan\n9. Quit\n")

    while True:
        choice = int(input("Which function would you like to perform?: "))
        if choice == 1:
            first = int(input("First number: "))
            second = int(input("Second number: "))
            print(first, " + ", second, " = ", add(first, second))
        elif choice == 2:
            first = int(input("First number: "))
            second = int(input("Second number: "))
            print(first, " - ", second, " = ", subtract(first, second))
        elif choice == 3:
            first = int(input("First number: "))
            second = int(input("Second number: "))
            print(first, " * ", second, " = ", multiply(first, second))
        elif choice == 4:
            first = int(input("First number: "))
            second = int(input("Second number: "))
            print(first, " / ", second, " = ", divide(first, second))
        elif choice == 5:
            first = int(input("Number: "))
            second = int(input("Exponent: "))
            print(first, "^", second, " = ", exponent(first, second))
        elif choice == 6:
            first = int(input("Hypotenuse: "))
            second = int(input("Opposite: "))
            print("Sin Theta = ", findSin(first, second))
        elif choice == 7:
            first = int(input("Hypotenuse: "))
            second = int(input("Adjesant: "))
            print("Cos Theta = ", findCos(first, second))
        elif choice == 8:
            first = int(input("Adjesant: "))
            second = int(input("Opposite: "))
            print("Tan Theta = ", findTan(first, second))
        elif choice == 9:
            sys.exit()
        
Calculator()
