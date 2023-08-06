import json
import os
import subprocess


def get_data_path(*path):
    current_folder = os.path.dirname(__file__)
    return os.path.join(current_folder, "data", *path)


def get_data(*path: str):
    path = get_data_path(*path)
    with open(path) as f:
        data = f.read()
    return data


def run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    return subprocess.run(cmd, stdout=stdout, stderr=stderr)


def load_database():
    json_tools = json.load(open(get_data_path("tools.json")))
    tools = {}
    for json_tool in json_tools:
        name = json_tool["name"]
        tools[name] = json_tool

    return tools


def is_root():
    return os.geteuid() == 0


def distinct_list(l):
    return list(dict.fromkeys(l))
