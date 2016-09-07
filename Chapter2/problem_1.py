import math


def input_coordinate():
    x1 = input("Enter the value of x1: ")
    y1 = input("Enter the value of y1: ")
    x2 = input("Enter the value of x2: ")
    y2 = input("Enter the value of y2: ")
    result(x1, x2, y1, y2)  # call result function with 4 arguments


def result(x1, x2, y1, y2):
    distance = math.sqrt(math.pow((int(x2) - int(x1)), 2) + math.pow((int(y2) - int(y1)), 2))
    print("The distance is: ", distance)


if __name__ == "__main__":
    input_coordinate()  # call input function
