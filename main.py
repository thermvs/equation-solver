from math import ceil
from sympy import symbols, sin, exp, cos, pi
from input import input_number, input_float
from solver import improved_euler_method
from graphics import make_graph


def main():
    x, y = symbols('x y')
    functions = [x ** 2 - 2 * y, sin(x), 1 + exp(-x) * cos(pi * x) - y]

    print("Improved Euler Method")
    num_of_diff_equation = input_number("Choose one of the differential equations:\n"
                                        "1) y' - x^2 - 2y = 0\n"
                                        "2) y' = sin(x)\n"
                                        "3) y' = 1 + e^(-x) * cos(pi * x) - y\n")

    function = functions[num_of_diff_equation - 1]
    x0 = input_float("Input start point\nx = ")
    y0 = input_float("y = ")
    xn = input_float("Input end point\n")
    precision = input_number("Input precision\n")
    h = 0.1 ** ceil(precision / 2)

    coords_x, coords_y = improved_euler_method(function, x0, y0, xn, h)
    make_graph(coords_x, coords_y)


if __name__ == "__main__":
    main()
