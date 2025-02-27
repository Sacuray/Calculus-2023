import numpy as np

def get_function(num):
    if (num == 1):
        return lambda x: x ** 3 - 3.125 * (x ** 2) - 3.5 * x + 2.458
    if (num == 2):
        return lambda x: x ** 2 - 3 * x - 2
    if (num == 3):
        return lambda x: np.sin(x) - np.cos(x) + 0.2*x

def get_function_name(num):
    if (num == 1):
        return "x^3 - 3.125x^2 - 3.5x + 2.458"
    if (num == 2):
        return "x^2 - 3x - 2"
    if (num == 3):
        return "sin(x) - cos(x) + 0.2x"


#-------Системы-------

def get_system_function(num):
    if (num == 1):
        return lambda x, y : x**2 + y**2 - 4
    if (num == 2):
        return lambda x, y : x**3 + y - 1
    if (num == 3):
        return lambda x, y: x**2 - y - 3

def get_system_function_name(num):
    if (num == 1):
        return "x^2 + y^2 - 4"
    if (num == 2):
        return "x^3 + y - 1"
    if (num == 3):
        return "x^2 - y - 3"