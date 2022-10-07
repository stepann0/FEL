import math

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
        error(f"can't generate range {start}..{stop}:{step}.")

def sequence(start, stop):
    step = 1
    if stop < start:
        step = -1
    return sequence_step(start, stop, step)
    
def sum_arr(arr):
    if len(arr) == 1 and isinstance(arr[0], list):
        arr = arr[0] 
    try:
        return sum(arr)
    except Exception:
        error(f"can't sum arr {arr}.")

def call_func(func_id, args):
    try:
        return FUNCTIONS[func_id](args)
    except Exception:
        error(f"some kind of error was occured when calling the function '{func_id}'")

FUNCTIONS = {
    "sum": sum_arr,
    "sin": math.sin,
    "cos": math.cos
}
