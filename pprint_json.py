import json


def load_data(func):
    def wrapped(filepath):
        try:
            file_handler = open(filepath, 'r', encoding='windows-1251')
            content_json = json.load(file_handler)
            func(content_json)
            file_handler.close()
        except ValueError:
            print('JSON file contain errors! ')
        except FileNotFoundError:
            print('Not found JSON file. Please check way. ')
    return wrapped


@load_data
def pretty_print_json(content_json):
    user_friendly_json = json.dumps(content_json, sort_keys=True,
                                    indent=4, ensure_ascii=False)
    print(user_friendly_json)


if __name__ == '__main__':
    input_way = input('Please enter full way to JSON file: ')
    pretty_print_json(input_way)
