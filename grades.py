"""Учебный калькулятор среднего балла. Оценки от 0 до 100."""

import math


def average_score(scores):
    """Вернуть средний балл; отклонить пустой список и неверные оценки."""
    values = list(scores)
    if not values:
        raise ValueError("Введите хотя бы одну оценку.")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Оценки должны быть числами.")
        if not math.isfinite(value) or not 0 <= value <= 100:
            raise ValueError("Оценки должны быть от 0 до 100.")
    return round(sum(values) / len(values), 2)


def main():
    print("Калькулятор среднего балла | Вариант 17")
    print("Введите оценки от 0 до 100 через пробел. Пример: 80 90 100")
    try:
        scores = [float(item) for item in input("Оценки: ").split()]
        print(f"Средний балл: {average_score(scores):.2f}")
    except ValueError as error:
        print(f"Ошибка: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
