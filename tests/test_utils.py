from unittest.mock import mock_open, patch

from src.utils import read_json_file



m = mock_open()


@patch("json.load")
def test_read_json_file(mock_json_load):
    m = mock_open()
    with patch("builtins.open", m) as mock_file_open:

        data = [{"amount": "100", "currency": "RUB"}]
        mock_json_load.return_value = data
        result = read_json_file("test")
        assert result == data
