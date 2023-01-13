"""
This is the main script, it contains four functions:
    - open_file: It opens the json file and returns the content as a dictionary.
    - get_dependencies: It returns the dependencies of the package.
    - get_dependency_graph: It returns the dependency graph.
    - print_graph: It prints the dependency graph.

When directly executed it asks for the path to the json and prints the dependency graph.
"""
import os
import argparse
import json
import sys
from collections.abc import Generator


def open_file(path: str = os.path.join(os.getcwd(), './src/cern_oa/tmp/deps.json')) \
        -> dict[str, list]:
    """
    It opens the json file and returns the content as a dictionary.
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
    :param package: Name of the package.
    :type package: str
    :param dependencies: Dictionary with the dependencies.
    :type dependencies: dict[str, list]
    :param depth: Depth of the package in the dependency graph.
    :type depth: int
    :return: Generator with the dependencies of the package.
    :rtype: Generator[tuple[str, int]]
    """
    if package in dependencies:
        for dependency in dependencies[package]:
            yield dependency, depth + 1
            yield from get_dependencies(dependency, dependencies, depth + 1)


def get_dependency_graph(dependencies: dict[str, list]) -> Generator[tuple[str, int]]:
    """
    It returns the dependency graph.
    :param dependencies: Dictionary with the dependencies.
    :type dependencies: dict[str, list]
    :return: Generator with the dependency graph.
    :rtype: Generator[tuple[str, int]]
    """
    for package in dependencies:
        yield package, 0
        yield from get_dependencies(package, dependencies, 0)


def print_graph(graph: Generator[tuple[str, int]]) -> None:
    """
    It prints the dependency graph.
    :param graph: Generator with the dependency graph.
    :type graph: Generator[tuple[str, int]]
    :return: None
    :rtype: None
    """
    for package, depth in graph:
        print("  " * depth + "- " + package)


def main():
    """
    It parses the argument file and prints the dependency graph.
    :return: None
    :rtype: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, help='Path to the json file.',
                        default=os.path.join(os.getcwd(), './src/cern_oa/tmp/deps.json'))
    file = open_file(parser.parse_args().file)
    print_graph(get_dependency_graph(file))


if __name__ == '__main__':
    main()
