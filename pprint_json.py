import json
import sys


def load_way_and_output_json_content():
    input_way = input('Please enter full way to JSON file '
                      'or type "exit" to close program: ')
    pretty_print_json(load_data(input_way)) if input_way is not 'exit' else sys.exit()


def load_data(input_way):
    try:
        with open(input_way, 'r', ) as file_handler:
            return json.load(file_handler)
    except Exception:
        return None


def pretty_print_json(load_data):
    if load_data is not None:
        user_friendly_json = json.dumps(load_data, sort_keys=True,
                                        indent=4, ensure_ascii=False)
        print(user_friendly_json)
    else:
        print("Error! Please check JSON file and directory way")
        load_way_and_output_json_content()


if __name__ == '__main__':
    load_way_and_output_json_content()
