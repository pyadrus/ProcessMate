
import json


def get_data_from_json():
    with open('data/tab_2024.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

data = get_data_from_json()

for key in data:
    print(f"Ключ: {key}")
    print(f"Значение: {data[key]}")