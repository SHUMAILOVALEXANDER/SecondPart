import csv
import json
input_filename = "input.csv"
output_filename = "output.json"
delimiter = ","
line_terminator = "\n"
with open(input_filename, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=delimiter)
    data = [row for row in csv_reader]
with open(output_filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
with open(output_filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4, ensure_ascii=False), end="")
