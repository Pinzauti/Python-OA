"""

"""
import os
import argparse
import json
import sys
from collections.abc import Generator


def open_file(path: str = os.path.join(os.getcwd(), './src/cern_oa/tmp/deps.json')) -> dict[str, list]:
    """
    It opens the file and returns the content as a dictionary.
    :param path: Path to the file.
    :type path: str
    :return: Content of the file.
    :rtype: dict[str, list]
    """
    try:
        with open(path, encoding='UTF-8') as file:
            dependencies = json.load(file)
    except FileNotFoundError:
        sys.stderr.write("The file path is incorrect.")
        sys.exit()
    return dependencies



