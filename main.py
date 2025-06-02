from src.external_api import convert_to_rub
from src.utils import read_json_file

if __name__=="__main__":
    data = read_json_file('data/operations.json')

    result = convert_to_rub(data, 'RUB')
    print(result)


