from json import JSONDecodeError
from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json_file


@patch("json.load")
def test_read_json_file(mock_json_load):
    m = mock_open()
    with patch("builtins.open", m) as mock_file_open:

        data = [{"amount": "100", "currency": "RUB"}]
        mock_json_load.return_value = data
        result = read_json_file("test")
        assert result == data


@patch("os.path.isfile", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value')")
def test_empty_file(mock_open, mock_isfile):
    file = "test_file.json"
    result = read_json_file(file)
    assert result == []
