# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    # YOUR CODE HERE
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    op = sys.argv[2]
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y




if __name__ == "__main__":
    print(main())
