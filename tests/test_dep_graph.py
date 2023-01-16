import pytest
from unittest.mock import mock_open, patch
from cern_oa.dep_graph import open_file, get_dependencies, get_dependency_graph


@pytest.fixture
def mock_file():
    m = mock_open(read_data='{"m_pkg1": ["m_pkg2", "m_pkg3"],"m_pkg2": ["m_pkg3"],"m_pkg3": []}')
    with patch('builtins.open', m):
        yield m


class TestOpenFile:
    def test_open_file(self, mock_file):
        assert open_file() == {"m_pkg1": ["m_pkg2", "m_pkg3"], "m_pkg2": ["m_pkg3"], "m_pkg3": []}


class TestGetDependencyGraph:
    def test_get_dependency_graph(self):
        assert list(
            get_dependency_graph({"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg3"], "pkg3": []})) == \
               [('pkg1', 0), ('pkg2', 1), ('pkg3', 2), ('pkg3', 1), ('pkg2', 0), ('pkg3', 1),
                ('pkg3', 0)]

    def test_get_dependency_graph_empty(self):
        assert list(get_dependency_graph({})) == []

    def test_get_dependency_graph_one(self):
        assert list(get_dependency_graph({"pkg1": []})) == [('pkg1', 0)]

    def test_get_dependency_graph_one_witha_one_dep(self):
        assert list(get_dependency_graph({"pkg1": ["pkg2"]})) == [('pkg1', 0), ('pkg2', 1)]

    def test_get_dependency_graph_two_with_two_deps(self):
        assert list(get_dependency_graph({"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg4", "pkg5"]})) == \
               [('pkg1', 0), ('pkg2', 1), ('pkg4', 2), ('pkg5', 2), ('pkg3', 1), ('pkg2', 0),
                ('pkg4', 1), ('pkg5', 1)]

    def test_get_dependency_graph_four_levels_with_one_dep(self):
        assert list(get_dependency_graph({"pkg1": ["pkg2"], "pkg2": ["pkg3"], "pkg3": ["pkg4"]})) == \
               [('pkg1', 0), ('pkg2', 1), ('pkg3', 2), ('pkg4', 3), ('pkg2', 0), ('pkg3', 1),
                ('pkg4', 2), ('pkg3', 0), ('pkg4', 1)]


class TestGetDependencies:
    def test_get_dependencies(self):
        assert list(
            get_dependencies("pkg1", {"pkg1": ["pkg2", "pkg3"], "pkg2": ["pkg3"], "pkg3": []},
                             0)) == \
               [('pkg2', 1), ('pkg3', 2), ('pkg3', 1)]

    def test_get_dependencies_empty(self):
        assert list(get_dependencies("pkg1", {}, 0)) == []

    def test_get_dependencies_one(self):
        assert list(get_dependencies("pkg1", {"pkg1": []}, 0)) == []

    def test_get_dependencies_one_with_one_dep(self):
        assert list(get_dependencies("pkg1", {"pkg1": ["pkg2"]}, 0)) == [('pkg2', 1)]

    def test_get_dependencies_one_with_two_deps(self):
        assert list(get_dependencies("pkg1", {"pkg1": ["pkg2", "pkg3"]}, 0)) == [('pkg2', 1),
                                                                                 ('pkg3', 1)]

    def test_get_dependencies_two_with_one_dep(self):
        assert list(get_dependencies("pkg1", {"pkg1": ["pkg2"], "pkg3": ["pkg4"]}, 0)) == [
            ('pkg2', 1)]
