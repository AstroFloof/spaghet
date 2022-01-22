# try to follow the order of https://greentreesnakes.readthedocs.io/en/latest/nodes.html#top-level-nodes
import ast


class BinOp(ast.BinOp):
    pass


class Add(ast.Add):
    # x + y
    pass


class Sub(ast.Sub):
    # x - y
    pass


class Mult(ast.Mult):
    # x * y
    pass


class Div(ast.Div):
    # x / y
    pass


class FloorDiv(ast.FloorDiv):
    # x // y
    pass


class Mod(ast.Mod):
    # x 5 y
    pass


class Pow(ast.Pow):
    # x ** y
    pass


class LShift(ast.LShift):
    # x << y
    pass


class RShift(ast.RShift):
    # x >> y
    pass


class BitOr(ast.BitOr):
    # x | y
    pass


class BitXor(ast.BitXor):
    # x ^ y
    pass


class BitAnd(ast.BitAnd):
    # x & y
    pass


class MatMult(ast.MatMult):
    # x @ y
    pass
