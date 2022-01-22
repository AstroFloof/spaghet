import ast


class Bytes(ast.Bytes):
    pass


class Constant(ast.Constant):
    pass


class Dict(ast.Dict):
    pass


class Num(ast.Num):
    pass


class Param(ast.Param):
    pass


class Set(ast.Set):
    # set()
    pass


class Str(ast.Str):
    # "" '' str()
    pass


class Tuple(ast.Tuple):
    # (t, )
    pass


class List(ast.List):
    pass
