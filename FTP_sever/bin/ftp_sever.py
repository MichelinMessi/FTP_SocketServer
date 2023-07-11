import os, sys
from core import main

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

if __name__ == '__main__':
    # print(sys.path)
    main.ArgvHandler()