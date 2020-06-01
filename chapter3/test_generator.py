import random
from typing import List


def generate_tests() -> List[int]:
    tests = [
        [],
        [0],
        [i for i in range(10)],
        [i for i in reversed(range(10))]
    ]
    # random with duplicates
    tests.extend([[random.randint(0, 15) for i in range(20)]
                  for j in range(10)])
    return tests
