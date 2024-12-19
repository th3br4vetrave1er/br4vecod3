from math import sqrt

message: str = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа'
)


def square_root(num: float) -> float:
    """Calculate square root."""
    return sqrt(num)


def calc(your_number: float) -> None:
    """Calculate square root if it's > 0 number."""
    if your_number <= 0:
        print("Вы ввели ноль или меньше ноля.")
    else:
        root = square_root(your_number)
        print(
            f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}'
              )


print(message)
calc(0)
