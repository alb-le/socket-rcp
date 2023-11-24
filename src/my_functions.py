from typing import Any


class MyFunctions:
    def __init__(self):
        self.functions = {
            'sum': self.my_sum,
            'min': self.my_min,
        }
    @staticmethod
    def my_sum(left: int, right: int) -> int:
        return left + right

    @staticmethod
    def my_min(left: Any, right: Any) -> bool:
        return min(left, right)


if __name__ == '__main__':
    my_sum(1, 2)
