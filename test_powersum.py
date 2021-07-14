import pytest
from powersum import powersum
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('n', 'k', 'check' [
    (2, 5, 33),
    (3, -1, 0),
    (2, 0, 2),
    (5, 4, 821),
    (0, 4, 0)
])
def test_powersum(n, k, check):
    assert powersum(n, k) == check