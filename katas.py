
def add(x, y):
    """ Return the result of adding x to y. """
    return x + y


def multiply(x, y):
    """ Return the result of multiplying x by y. """
    result = 0

    for _ in range(x):
        result = add(result, y)

    return result


def power(x, n):
    """ Return the result of taking x to the nth power. """
    result = 1

    for _ in range(n):
        result = multiply(result, x)

    return result


def factorial(n):
    """ Return the result of calculating the factorial of n. """
    result = 1

    for i in range(1, n + 1):
        result = multiply(result, i)

    return result


def fibonacci(n):
    """ Return the nth number in the fibonacci sequence (starting at 0). """
    if n < 3:
        return n - 1
    else:
        second_to_last = 0
        last = 1
        result = 1

        for _ in range(2, n):
            result = second_to_last + last
            second_to_last, last = last, result

        return result
