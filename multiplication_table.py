print("Multiplication table")


def print_table(number, start=1, end=10):
    for counter in range(start, end+1, 1):
        print(f"{number} X {counter} = {number*counter}")


print_table(7)
print_table(10, 10, 20)
