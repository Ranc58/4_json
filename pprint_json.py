import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print('file not exist')
    with open(filepath, 'r', encoding='windows-1251') as file_handler:
        content_json = json.load(file_handler)
        user_friendly_json = pretty_print_json(content_json)
        print(user_friendly_json)


def pretty_print_json(data):
    decode_json = json.dumps(data, sort_keys=True,
                             indent=4, ensure_ascii=False)
    return decode_json


if __name__ == '__main__':
    pass

input_way = input('Please enter way to JSON: ')
load_data(input_way)
