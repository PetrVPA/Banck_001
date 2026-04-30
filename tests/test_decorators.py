from src.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


def test_log_to_file1():
    my_function(6, 3)
    file = open("mylog.txt", "r")
    file.seek(0)
    stend = file.readline()
    file.close()
    assert stend == "my_function ok\n"


def test_log_to_file2():
    my_function(6, 0)
    file = open("mylog.txt", "r")
    file.seek(0)
    stend = file.readline()
    file.close()
    assert stend == "my_function error: ZeroDivisionError. Inputs: (6, 0), {}\n"


def test_log_to_file3():
    my_function(6, "t")
    file = open("mylog.txt", "r")
    file.seek(0)
    stend = file.readline()
    file.close()
    assert stend == "my_function error: TypeError. Inputs: (6, t), {}\n"


@log()
def example_function(x, y):
    return x / y


def test_log_decorator1(capsys):
    result = example_function(6, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "my_function ok\n" in captured.out


def test_log_decorator2(capsys):
    result = example_function(6, "t")
    captured = capsys.readouterr()
    assert result is None
    assert "my_function error: TypeError. Inputs: (6, t), {}" in captured.out


def test_log_decorator3(capsys):
    result = example_function(2, 0)
    captured = capsys.readouterr()
    assert result is None
    assert "my_function error: ZeroDivisionError. Inputs: (2, 0), {}" in captured.out
