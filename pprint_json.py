import json
import sys


def load_data(input_way):
    try:
        with open(input_way, 'r', encoding='UTF-8') as file_handler:
            content_json = json.load(file_handler)
    except (ValueError, FileNotFoundError) as error:
        print(error)
        sys.exit()
    return content_json


def pretty_print_json(input_way):
    content_json = load_data(input_way)
    user_friendly_json = json.dumps(content_json, sort_keys=True,
                                    indent=4, ensure_ascii=False)
    print(user_friendly_json)


if __name__ == '__main__':
    input_way = input('Please enter full way to JSON file: ')
    pretty_print_json(input_way)
