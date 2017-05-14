import json
import sys


def start_program():
    input_way = input('Please enter full way to JSON file '
                      'or type "exit" to close program: ')
    load_data(input_way) if input_way != 'exit' else sys.exit()


def load_data(input_way):
    try:
        with open(input_way, 'r', encoding='UTF-8') as file_handler:
            content_json = json.load(file_handler)
            pretty_print_json(content_json)
    except (ValueError, FileNotFoundError) as error:
        print(error)
    finally:
        start_program()


def pretty_print_json(content_json):
    user_friendly_json = json.dumps(content_json, sort_keys=True,
                                    indent=4, ensure_ascii=False)
    print(user_friendly_json)


if __name__ == '__main__':
    start_program()
