PREFIX = "\033["
BOLD_CODE = "01"
ITALIC_CODE = "03"
UNDERLINE_CODE = "04"
REVERSE_CODE = "07"

JUST_BOLD = "01m"
RED = "38;05;196m"
BLUE = "38;05;111m"
GREEN = "38;05;35m"
YELLOW = "38;05;227m"
GRAY = "38;05;244m"
CYAN = "38;05;85m"
BACK = "\033[0m"

style_codes = {
    "i": ITALIC_CODE,
    "u": UNDERLINE_CODE,
    "b": BOLD_CODE,
    "r": REVERSE_CODE,
}

def apply_styles(color, styles):
    for s in styles:
        try:
            color = style_codes[s]+";"+color
        except KeyError:
            continue
    return color

def wrap(color):
    def func(s, styles=None):
        if len(s) == 0:
            return ""
        if styles:
            return PREFIX + apply_styles(color(), styles) + s + BACK
        return PREFIX + color() + s + BACK
    return func

@wrap
def bold(s="", styles=None):
    return JUST_BOLD

@wrap
def red(s="", styles=None):
    return RED

@wrap
def yellow(s="", styles=None):
    return YELLOW

@wrap
def blue(s="", styles=None):
    return BLUE

@wrap
def green(s="", styles=None):
    return GREEN

@wrap
def dim(s="", styles=None):
    return GRAY

@wrap
def cyan(s="", styles=None):
    return CYAN