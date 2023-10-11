import ast
from pylint.interfaces import IAstroidChecker

def register(linter):
    pass

def hello_detector(node):
    """
    Custom rule to detect 'hello' in the code.
    """
    if "hello" in node.value:
        yield (1, "C9999 Custom warning: 'hello' found in code")

hello_detector.name = "hello-detector"

def plugin():
    return astroid.checkers.wrap_checker(hello_detector)
