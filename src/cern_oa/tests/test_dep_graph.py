import pytest
from unittest.mock import mock_open, patch
from src.cern_oa.dep_graph import open_file, get_dependencies, get_dependency_graph


@pytest.fixture
def mock_file():
    m = mock_open(read_data='{"m_pkg1": ["m_pkg2", "m_pkg3"],"m_pkg2": ["m_pkg3"],"m_pkg3": []}')
    with patch('builtins.open', m):
        yield m


class TestOpenFile:
    def test_open_file(self, mock_file):
        assert open_file() == {"m_pkg1": ["m_pkg2", "m_pkg3"], "m_pkg2": ["m_pkg3"], "m_pkg3": []}



