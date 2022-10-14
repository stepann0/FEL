BOLD = "\033[01m"
RED = "\033[38;05;196m"
BLUE = "\033[38;05;70m"
GREEN = "\033[38;05;35m"
YELLOW = "\033[38;05;227m"
GRAY = "\033[38;05;244m"
BOLD_BLUE = "\033[01;38;05;68m"
BACK = "\033[0m"

def reset(color_func):
    def reset_style(s):
        return color_func(s) + BACK
    return reset_style

@reset
def bold(s):
    return BOLD+s

@reset
def red(s):
    return RED+s

@reset
def yellow(s):
    return YELLOW+s

@reset
def blue(s):
    return BLUE+s

@reset
def bold_blue(s):
    return BOLD_BLUE+s

@reset
def dim(s):
    return GRAY+s
