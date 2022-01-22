import ast


class Comprehension(ast.comprehension):
    pass


class ListComp(ast.ListComp):
    # [x for x in xs]
    pass


class SetComp(ast.SetComp):
    # {x for x in xs}
    pass


class GeneratorExp(ast.GeneratorExp):
    # (x for x in xs)
    # optional parens
    pass


class DictComp(ast.DictComp):
    pass
