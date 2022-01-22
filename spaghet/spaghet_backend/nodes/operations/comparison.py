# try to follow the order of https://greentreesnakes.readthedocs.io/en/latest/nodes.html#top-level-nodes
import ast


class Compare(ast.Compare):
    pass


class Eq(ast.Eq):
    # x == y
    pass


class NotEq(ast.NotEq):
    # x != y
    pass


class Lt(ast.Lt):
    # x < y
    pass


class LtE(ast.LtE):
    # x <= y
    pass


class Gt(ast.Gt):
    # x > y
    pass


class GtE(ast.GtE):
    # x >= y
    pass


class Is(ast.Is):
    # x is y
    pass


class IsNot(ast.IsNot):
    # x is not y
    pass


class In(ast.In):
    # x in y
    pass


class NotIn(ast.NotIn):
    # x not in y
    pass
