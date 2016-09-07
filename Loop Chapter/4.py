def take_input():
    n = int(input("Enter your range: "))
    code(n)


def code(n):
    i = temp = 1
    total = 0
    while i <= n:
        j = 1
        while j <= i:
            total += temp
            temp += 1
            j += 1
        i += 1
    return show_result(total)


def show_result(total):
    print("Total is: ", total)


if __name__ == "__main__":
    take_input()
