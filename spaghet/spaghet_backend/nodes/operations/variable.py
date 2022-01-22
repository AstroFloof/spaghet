import ast


class Name(ast.Name):
    pass


class Load(ast.Load):
    # x
    pass


class Store(ast.Store):
    # x = y
    pass


class Del(ast.Del):
    # del x
    pass


class Starred(ast.Starred):
    # *splat
    pass


class AugLoad(ast.AugLoad):
    # what's this
    pass


class AugStore(ast.AugStore):
    # what's this
    pass


class Await(ast.Await):
    # whoosh you forgot it
    pass
