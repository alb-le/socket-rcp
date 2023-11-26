from typing import Any


class FunctionsImplementation:
    def __init__(self):
        self.functions = {
            'help': self.__help,
            'sum': self.__my_sum,
            'min': self.__my_min,
        }

    def __help(self):
        return f"List of possible functions: {self.functions.keys()}"

    @staticmethod
    def __my_sum(left: int, right: int) -> int:
        return left + right

    @staticmethod
    def __my_min(left: Any, right: Any) -> bool:
        return min(left, right)

    def run_fn(self, request):
        function_name, args, kwargs = request
        return self.functions[function_name.lower()](*args, **kwargs)
