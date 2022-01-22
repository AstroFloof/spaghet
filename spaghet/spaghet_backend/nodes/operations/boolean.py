# try to follow the order of https://greentreesnakes.readthedocs.io/en/latest/nodes.html#top-level-nodes
import ast


class BoolOp(ast.BoolOp):
    pass


class And(ast.And):
    pass


class Or(ast.Or):
    pass
