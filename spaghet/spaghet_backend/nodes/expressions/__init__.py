from .subscripting import *
from .comprehensions import *


class Expr(ast.Expr):
    pass


class NamedExpr(ast.NamedExpr):
    pass


class Call(ast.Call):
    # func(args, keywords, starred_args, kwargs)
    pass


class CallKwarg(ast.keyword):
    # f(x=x)
    pass


class IfExp(ast.IfExp):
    # x if b else y
    pass


class Attribute(ast.Attribute):
    # x.y
    pass
