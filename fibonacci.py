"""Fibonacci sequence - with and without recursion."""

def with_recursion(num1, num2, limit=1000000):
    print(str(num1))
    num1, num2 = num2, num1 + num2

    if num1 < limit:
        with_recursion(num1, num2, limit)

def without_recursion(num1, num2, limit=1000000):
    def fibonacci(a, b):
        a, b = b, a + b
        return a, b

    while num1 < limit:
        print(num1)
        nums = fibonacci(num1, num2)
        num1, num2 = nums[0], nums[1]


def main():
    print('With recursion:')
    with_recursion(0, 1, 200)
    print('Without recursion:')
    without_recursion(0, 1, 200)

if __name__ == "__main__":
    main()