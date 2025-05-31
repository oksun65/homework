import json


def read_json_file(input_file):
    with open(input_file, 'r', encoding='UTF-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

        if data == '':
           return []

        return data


if __name__ == "__main__":
    lst = read_json_file('data/operations.json')
    print(lst)