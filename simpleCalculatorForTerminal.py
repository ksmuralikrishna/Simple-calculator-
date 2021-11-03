#   function for calculation
def addition(x, z):
    a = x + z
    return a


def subtraction(x, z):
    a = x - z
    return a


def multiplication(x, z):
    a = x * z
    return a


def division(x, z):
    a = x / z
    return a


#   accept user input
def cal():
    num1 = int(input("Enter the  First Number  : "))

    num2 = int(input("Enter the second Number  : "))

    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    choice = input("Enter your choice :")

    listofchoice = ("1", "2", "3", "4")
    if choice == listofchoice[0]:
        print("\n\tResult\n----------------------")
        print(num1, "+", num2, "=", addition(num1, num2))
        return continuation()

    elif choice == listofchoice[1]:
        print("\n\tResult\n----------------------")
        print(num1, "-", num2, "=", subtraction(num1, num2))
        return continuation()

    elif choice == listofchoice[2]:
        print("\n\tResult\n----------------------")
        print(num1, "x", num2, "=", multiplication(num1, num2))
        return continuation()

    elif choice == listofchoice[3]:
        print("\n\tResult\n----------------------")
        print(num1, "/", num2, "=", division(num1, num2))
        return continuation()

    else:
        listz = ["please enter a valid number"]
        return "\n".join(listz)


def continuation():
    print("Do you want to continue ?\ny/n ")
    choice2 = input(":")
    if choice2 == "y":
        print(cal())
    else:
        return "\n".join(listx)

# calling calculation function


listx = ["Thank you"]

print(cal())
