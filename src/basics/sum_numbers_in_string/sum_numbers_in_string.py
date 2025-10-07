import re


def sum_numbers_in_string(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.

    Args:
        input_string: Строка, в которой нужно найти числа.

    Returns:
        Сумма всех найденных целых чисел.
    """
    total: int = 0
    i: int = 0
    n: int = len(input_string)
    while i < n:
        char: str = input_string[i]
        if char.isdigit() or (
            char == "-" and i + 1 < n and input_string[i + 1].isdigit()
        ):
            start: int = i
            i += 1
            while i < n and input_string[i].isdigit():
                i += 1
            total += int(input_string[start:i])
        else:
            i += 1
    return total


def sum_numbers_in_string_regex(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.

    Args:
        input_string: Строка, в которой нужно найти числа.

    Returns:
        Сумма всех найденных целых чисел.
    """
    tokens: list[str] = re.findall(r"\d+", input_string)
    return sum(int(token) for token in tokens)
