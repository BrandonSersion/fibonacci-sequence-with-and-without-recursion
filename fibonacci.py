"""Fibonacci sequence - with and without recursion."""

def with_recursion(num1, num2, limit=1000000):
    print(str(num1))
    temp = num1
    num1 = num2
    num2 = temp + num2

    if num1 < limit:
        with_recursion(num1, num2, limit)

def without_recursion(num1, num2, limit=1000000):
    def fibonacci(a, b):
        temp = a
        a = b
        b = temp + a
        return a, b

    while num1 < limit:
        print(num1)
        return_nums = fibonacci(num1, num2)
        num1, num2 = return_nums[0], return_nums[1]


def main():
    print('With recursion:')
    with_recursion(0, 1, 200)
    print('Without recursion:')
    without_recursion(0, 1, 200)

if __name__ == "__main__":
    main()