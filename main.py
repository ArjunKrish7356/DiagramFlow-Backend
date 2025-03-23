import ast
import os
import json
from parser_pyfile import parse_python_file

codebase = {
    "files": {},
    "dependencies": [],
    "indexes": {
        "class_names": {},
        "function_names": {},
        "imports": {}
    }
}



def process(file_path):
    """Take the filepath and check if python then pass it to ast converter"""
    print(2)
    if file_path.endswith('.py'):
        parse_python_file(codebase, file_path)

        

def dfs_traverse_directory(directory: str):
    """Traverse directory using os.walk (which handles recursion)"""
    print(1)
    for root, dirs, files in os.walk(directory):
        for file in files:
            process(os.path.join(root, file))


if __name__ == "__main__":
    dfs_traverse_directory("./DirectoryToConvert")
    with open("./formats/codebase.json", "w") as f:
        json.dump(codebase, f, indent=2)