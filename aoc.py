import sys
import os
import importlib

def main():
    days = next(os.walk('.'))[1][1:]
    selected = sys.argv[1] if (len(sys.argv) == 2) else ''

    if (selected != ''):
        importlib.import_module(selected)
    else:
        for day in days:
            importlib.import_module(day)

main()
