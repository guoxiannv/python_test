def fibonacci(n):
    """
    计算斐波那契数列的第n项
    斐波那契数列: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(n):
    """
    生成斐波那契数列的前n项
    """
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci_sequence(5))
