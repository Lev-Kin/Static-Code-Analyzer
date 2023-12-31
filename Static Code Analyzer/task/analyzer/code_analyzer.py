import os.path
import sys
from operator import attrgetter
from typing import List, Iterable

from linters import LinterError, Linters


def main():
    errors: List[LinterError] = []
    names = get_python_file_names(sys.argv[1])
    for name in names:
        with open(name, 'r') as f:
            text = f.readlines()
        errors.extend(Linters.examine_text(text, name))

    if errors:
        errors.sort(key=attrgetter('file_name', 'line_number', 'code'))
        print(*errors, sep='\n')


def get_python_file_names(path: str) -> Iterable[str]:
    names = []
    if os.path.isfile(path):
        names = [path] if path.endswith('.py') else []
    for dir_name, _, files in os.walk(path):
        names.extend(os.path.join(dir_name, f) for f in files)
    return (name for name in names if name.endswith('.py')
            # SHAME on the project creator for making me write this line!
            and not name.endswith('/tests.py'))


if __name__ == '__main__':
    main()