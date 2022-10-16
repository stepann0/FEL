import numpy as np
import colors

def error(msg):
    print(colors.red(f"Error: {msg}"))

def describe(obj):
    print(obj, type(obj))

def compare(s1, op, s2):
    if op == '<':
        return s1 < s2
    elif op == '>':
        return s1 > s2
    elif op == '<=':
        return s1 <= s2
    elif op == '>=':
        return s1 >= s2
    elif op == '==':
        return s1 == s2
    elif op == '!=':
        return s1 != s2

def bin_op(s1, op, s2):
    if op == '+':
        return s1 + s2
    elif op == '-':
        return s1 - s2
    elif op == '*':
        return s1 * s2
    elif op == '/':
        return s1 / s2
    elif op == '%':
        return s1 % s2
    elif op == '^':
        return s1 ** s2

def sequence_step(start, stop, step):
    try:
        return np.arange(start, stop, step)
    except Exception:
        error(f"can't generate range {start}:{stop}:{step}.")

def sequence(start, stop):
    step = 1
    if stop < start:
        step = -1
    return sequence_step(start, stop, step)

def call_func(func_id, args):
    try:
        return FUNCTIONS[func_id](*args)
    except (TypeError, ValueError):
        error(f"error in function '{func_id}' arguments")
    except KeyError:
        error(f"function '{func_id}' not implemented")

FUNCTIONS = {
    "sum": np.sum,
    "prod": np.prod,
    "avr": np.average,
    "median": np.median,
    "mean": np.mean,
    "std": np.std,
    "var": np.var,
    "sort": np.sort,
    "mean": np.mean,
    "matmul": np.matmul,
    "rng" : np.arange,
    "max": np.amax,
    "min": np.amin,

    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "hypot": np.hypot,
    "degrees": np.degrees,
    "floor": np.floor,
    "ceil": np.ceil,
    "pow": np.power,
    "factorial": np.math.factorial,
    "sqrt": np.sqrt,
}
