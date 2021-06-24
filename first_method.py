print("Simple method")


def print_hello_world_twice():
    print_hello_world(2)


def print_hello_world(times):
    for i in range(1, times + 1):
        print("Hello Python! Mr. " + str(i))


def print_square(number):
    print("Square of " + str(number) + " is " + str(number * number))


def print_squares(limit):
    for counter in range(1, limit+1):
        print_square(counter)


def print_squares_of_even(limit):
    for counter in range(2, limit+1,2):
        if counter % 2 == 0:
            print_square(counter)


def print_in_reverse(limit):
    for i in range(limit, 0, -1):
        print(i)


# print_in_reverse(10)
print_squares_of_even(4)
# print_squares(4)
# print("Execute before function")
# print_hello_world_twice()
# print_hello_world(4)
