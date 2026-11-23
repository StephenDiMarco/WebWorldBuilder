from json.decoder import JSONDecodeError
import random
import json
import os

def capitalize_sentences(text):
    return ". ".join([s[0].upper() + s[1:] if s else "" for s in text.split(". ")])

def prefix_indefinite_artile_on_possible_plural(string_content):
    if string_content.lower().endswith('s'):
        return string_content
    else:
        return prefix_indefinite_article(string_content)

def prefix_indefinite_article(string_content):
    if string_content.lower().startswith(('a', 'e', 'i', 'o', 'u', 'y')):
        return "an " + string_content
    return "a " + string_content

def load_json(abs_file_path):
    json_data = {}
    if os.path.exists(abs_file_path):
        with open(abs_file_path, 'r') as json_file:
            try:
                json_data = json.load(json_file)
            except JSONDecodeError as e:
                print("Error: " + str(e))
        return json_data
    else:
        print(f"Error: {abs_file_path} does not exist.")
        return json_data

def select_random_list_value(list_to_select_from):
    return random.choice(list_to_select_from)