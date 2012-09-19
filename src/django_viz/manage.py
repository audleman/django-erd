#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
    BASE_PATH = SOURCE_PATH
    for i in range(2):
        BASE_PATH = os.path.dirname(BASE_PATH)
    sys.path.insert(0, os.path.join(BASE_PATH, 'lib'))
    sys.path.insert(0, os.path.join(BASE_PATH, 'src'))
    sys.path.insert(0, SOURCE_PATH)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_viz.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
