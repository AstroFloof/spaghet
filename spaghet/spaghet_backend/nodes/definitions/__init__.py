from .func import *
from .coro import *


class Global(ast.Global):
    pass


class Nonlocal(ast.Nonlocal):
    pass


class ClassDef(ast.ClassDef):
    pass
