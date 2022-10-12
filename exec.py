import numpy as np

def error(msg):
    print("\033[31m"+"Error: "+msg+"\033[0m")

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
        return list(range(start, stop, step))
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
    "avr": np.average,
    "median": np.median,
    "mean": np.mean,
    "std": np.std,
    "var": np.var,
    "sort": np.sort,
    "mean": np.mean,
    "matmul": np.matmul,

    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "hypot": np.hypot,
    "degrees": np.degrees,
    "floor": np.floor,
    "ceil": np.ceil,
}
