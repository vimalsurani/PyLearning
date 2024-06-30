# Multiple Decorators
# Example of deco to calculate the time difference between start and end of a function
import time

n = int(input("Enter a number: "))


def my_timer_2(func):
    def wrapper():
        print("execute the function")
        func()

    return wrapper


def my_timer_1(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("time take to execute the function is: ", end_time - start_time)

    return wrapper


@my_timer_1
@my_timer_2
def squares():
    result = n ** 2
    print(f"The square of the number {n} is: {result}")
    time.sleep(1)


squares()
