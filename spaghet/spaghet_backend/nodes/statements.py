import ast


class Assign(ast.Assign):
    pass


class AnnAssign(ast.AnnAssign):
    pass


class AugAssign(ast.AugAssign):
    pass


class Raise(ast.Raise):
    pass


class Assert(ast.Assert):
    pass


class Delete(ast.Delete):
    pass


class Pass(ast.Pass):
    pass  # ironic


class Import(ast.Import):
    pass


class ImportFrom(ast.ImportFrom):
    pass


class ImportedName(ast.alias):
    pass
