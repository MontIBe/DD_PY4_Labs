# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:  # функция открытия
        data = json.load(file) # функция загрузки файла

    total_sum = 0

    for entry in data:
        score = entry.get("score", 0)  # извлечение значения "score" и "weight"
        weight = entry.get("weight", 0)

        total_sum += score * weight

    return round(total_sum, 3)

print(task())

