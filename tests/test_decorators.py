import pytest
from src.decorators import log

def test_filter_by_log1(question_test_log1, answer_test_log1):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y
    assert log(question_test_log1) == answer_test_log1
    with pytest.raises(TypeError, match="my_function error: TypeError. Inputs: (1, t), {}"):
        log(filename="mylog.txt")