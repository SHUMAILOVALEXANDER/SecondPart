import json
def calculate_sum_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    total_sum = 0.0
    for item in data:
        total_sum += item["score"] * item["weight"]
        # print(f'{total_sum} = {item["score"]} * {item["weight"]}')
    # print(round(total_sum, 3))
    return round(total_sum, 3)
print(calculate_sum_from_json("input.json"))
