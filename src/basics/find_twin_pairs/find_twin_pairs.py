import math


def find_twin_pairs(X: list[list[int]], threshold: float):
    """
    Находит все пары объектов, у которых евклидово расстояние меньше threshold.

    Аргументы:
    X -- двумерный список чисел (n x m)
    threshold -- пороговое значение расстояния

    Возвращает:
    Список кортежей (i, j, distance), где i < j и distance < threshold
    """
    if not X or not X[0]:
        return []
    result = []
    for i, row_i in enumerate(X):
        for j, row_j in enumerate(X[i + 1 :], start=i + 1):
            dist_sq: float = sum((a - b) ** 2 for a, b in zip(row_i, row_j))
            if dist_sq <= threshold**2:
                result.append((i, j, math.sqrt(dist_sq)))
    return result
