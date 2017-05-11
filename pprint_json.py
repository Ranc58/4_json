import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print('file not exist')
    with open(filepath, 'r', encoding='UTF-8') as file_handler:
        data = json.load(file_handler)
        decode_json = pretty_print_json(data)
        print(decode_json)


def pretty_print_json(data):
    decode_json = json.dumps(data, sort_keys=True,
                             indent=4, ensure_ascii=False)
    return decode_json


if __name__ == '__main__':
    pass

input_way = input('Please enter way to JSON: ')
load_data(input_way)

