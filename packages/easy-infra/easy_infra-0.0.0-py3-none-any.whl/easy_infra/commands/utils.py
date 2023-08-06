import os
import os.path
import sys
import yaml
import glob


def current_directory_path():
    directory_path = os.getcwd()
    return directory_path


def file_exists(file_path):
    return os.path.exists(file_path)


def process_yaml(yaml_file):
    """Process yaml file"""

    with open(yaml_file, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return data


def find_key_in_file(key):
    """Find key in yaml file"""
    with open("easy.yml", "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            die(exc)
        else:
            return data[key]


def find_key_in_data(data, key):
    """Find key in data"""
    try:
        if data[key]:
            return data[key]
    except KeyError:
        die("Could not find key")


def replace_in_text_file(file_path, find, replace):
    """Replace text in text file"""
    # line = line.replace('this', '')
    with open(file_path, "r+") as file:
        text = file.read()
        text = text.replace(find, replace)
        file.seek(0)
        file.write(text)
        file.truncate()


def find_terraform_files():
    """Find terraform files"""
    files = []
    try:
        files = glob.glob("**/*.tf", recursive=True)
    except FileNotFoundError:
        die("Could not find terraform files")
    else:
        return files


def die(message):
    print(message)
    sys.exit(1)
