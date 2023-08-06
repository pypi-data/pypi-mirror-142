import fire  # type: ignore
from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> int:
    return int(a + b)


def subtract_numbers(a, b):
    return a - b


def main():
    fire.Fire(add_numbers)


if __name__ == "__main__":
    main()
