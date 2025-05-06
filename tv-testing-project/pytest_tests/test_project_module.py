import pytest
from  project_main import project_module

@pytest.mark.parametrize("values,expected_results",[])
def test_rolling_average():

    values1 = [1, 2, 3, 4, 5]
    period1 = 3
    values2 = [6, 7, 8, 9]
    period2 = 2
    result = project_module.rolling_average([1,2,3,4,5,6,],3)
    assert result == [2.0,3.0,4.0,5.0]

    result1 = project_module.rolling_average(values1,3)
    assert result == [2.0,3.0,4.0,5.0]
    # Act
    result2 = project_module.rolling_average(values2, period2)

   # Assert
    expected = [2.0, 3.0, 4.0]
    assert result == expected

