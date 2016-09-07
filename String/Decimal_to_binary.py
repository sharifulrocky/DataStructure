def convert(number):
    if number != 0:
        convert(number // 2)
    print(number % 2, end=" ")


def take_input():
    dec = int(input("Enter a decimal number: "))
    convert(dec)


if __name__ == "__main__":
    take_input()
