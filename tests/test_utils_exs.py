from unittest.mock import patch
from unittest.mock import Mock
from src.utils_exs import work_csv
from src.utils_exs import work_exel
import os


def test_work_csv1():
    # Настраиваем заглушку — мокаем csv_result
    mock_csv_result = Mock(return_value=[{'id': 1650703, 'state': 'EXECUTED'}])
    work_csv = mock_csv_result

    assert work_csv(os.path.join(os.path.dirname(__file__), '..', 'data',
                                 'test_excel.csv')) == [{'id': 1650703, 'state': 'EXECUTED'}]
    mock_csv_result.assert_called_once()

def test_work_exe1():
    # Настраиваем заглушку — мокаем ex_result
    mock_ex_result = Mock(return_value=[{'id': 1650703, 'state': 'EXECUTED'}])
    work_exel = mock_ex_result

    assert work_exel(os.path.join(os.path.dirname(__file__), '..', 'data',
                                 'test_excel.xlsx')) == [{'id': 1650703, 'state': 'EXECUTED'}]
    mock_ex_result.assert_called_once()

@patch('src.utils_exs')
def test_work_exe2(mock_ex_result):
    # Настраиваем заглушку — мокаем ex_result
    mock_ex_result.return_value = [{'id': 1650703, 'state': 'EXECUTED'}]
    zerro = work_exel(os.path.join(os.path.dirname(__file__), '..', 'data','test_excel.xlsx'))
    assert zerro == [{'id': 1650703, 'state': 'EXECUTED'}]

@patch('src.utils_exs')
def test_work_csv2(mock_csv_result):
    # Настраиваем заглушку — мокаем csv_result
    mock_csv_result.return_value = [{'id': 1650703, 'state': 'EXECUTED'}]
    zerro = work_csv(os.path.join(os.path.dirname(__file__), '..', 'data','test_excel.csv'))
    assert zerro == [{'id': 1650703, 'state': 'EXECUTED'}]
