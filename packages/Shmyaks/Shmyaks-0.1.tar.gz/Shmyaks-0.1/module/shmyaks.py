import json
import os


def read():
    with open(os.path.abspath('module/file.json')) as file:
        return json.dumps(file.read())


def to_do(func):
    func()


print(read())
