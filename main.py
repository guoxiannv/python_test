def fibonacci(position):
    """
    计算斐波那契数列的第position项
    斐波那契数列: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)

def fibonacci_sequence(count):
    """
    生成斐波那契数列的前count项
    """
    sequence = []
    for i in range(count):
        sequence.append(fibonacci(i))
    return sequence

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci_sequence(5))
