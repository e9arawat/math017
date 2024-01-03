"""importing solver function form solver.py file"""
from solver import solver


def answer():
    """calling solver function"""
    return solver(1, 1000)


if __name__ == "__main__":
    print(answer())
