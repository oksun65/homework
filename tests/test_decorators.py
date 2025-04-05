import os

from src.decorators import log


def test_log_exist_fle(filename="log.txt", directory="data"):

    @log(filename)
    def func(x):
        return x**2

    func(2)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    with open(filename, "r", encoding="UTF-8") as file:
        assert file.readline() == "func is ok.\n"


def test_log_consol_error(capsys):
    @log()
    def division_num(x):
        return 5 / x

    division_num(0)
    captured = capsys.readouterr()
    assert captured.out == "division_num error: ZeroDivisionError: division by zero. Input: (0,), {}.\n"
