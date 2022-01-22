import ast


class Subscript(ast.Subscript):
    # superclass for Index, Slice, and ExtSlice
    pass


class Index(ast.Index):
    # l[x]
    pass


class Slice(ast.Slice):
    # l[x:y]
    pass


class ExtSlice(ast.ExtSlice):
    # multiple Slice/Index in one expr
    pass
