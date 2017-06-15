#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
os.system('export PYTHONPATH=/usr/bin/python3:' +
          os.path.dirname(os.path.realpath(__file__)))

from interface.main_menu import MainMenu


def main():
    MainMenu()


if __name__ == '__main__':
    main()
