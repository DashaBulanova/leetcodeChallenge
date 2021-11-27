import pytest

from solution import find_max_cpu_load, job

@pytest.mark.parametrize("input, expected", [
([[1,4,3], [2,5,4], [7,9,6]], 7),
([[6,7,10], [2,4,11], [8,12,15]], 15),
([[1,4,2], [2,4,1], [3,6,5]], 8)
    ])
def test(input, expected):
    jobs = []
    for j in input:
        jobs.append(job(j[0], j[1], j[2]))
    actual = find_max_cpu_load(jobs)
    assert actual == expected