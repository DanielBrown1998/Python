from pathlib import Path

FILE_PATH = str(Path(__file__).parent.parent) + '\\file.txt'

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    print(file.readlines())
