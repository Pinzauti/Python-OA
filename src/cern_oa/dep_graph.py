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


def get_dependencies(package: str, dependencies: dict[str, list], depth: int) \
        -> Generator[tuple[str, int]]:
    """
    It returns the dependencies of the package.
    :param package:
    :type package:
    :param dependencies:
    :type dependencies:
    :param depth:
    :type depth:
    :return:
    :rtype:
    """
    if package in dependencies:
        for dependency in dependencies[package]:
            yield dependency, depth + 1
            yield from get_dependencies(dependency, dependencies, depth + 1)


def get_dependency_graph(dependencies: dict[str, list]) -> Generator[tuple[str, int]]:
    """

    :param dependencies:
    :type dependencies:
    :return:
    :rtype:
    """
    for package in dependencies:
        yield package, 0
        yield from get_dependencies(package, dependencies, 0)


def print_graph(graph: Generator[tuple[str, int]]) -> None:
    """

    :param graph:
    :type graph:
    :return:
    :rtype:
    """
    for package, depth in graph:
        print("  " * depth + "- " + package)


def main():
    """

    :return:
    :rtype:
    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-f', '--file', type=str, help='Path to file with dependencies',
                        default=os.path.join(os.getcwd(), './src/cern_oa/tmp/deps.json'))
    file = open_file(parser.parse_args().file)
    print_graph(get_dependency_graph(file))


if __name__ == '__main__':
    main()
