from typing import Any, Generator


from mypy.nodes import AssignmentStmt, FuncDef, ClassDef, Decorator
from mypy.options import Options
from mypy.parse import parse
from mypy.types import Type, AnyType, UnionType

def pluralize(word: str) -> str:
    if word[-1] in "sx" or word[-2:] in ["sh", "ch"]:
        return word + "es"
    return word + "s"

def _describe(thing: Type, a: bool = True) -> str:


    if isinstance(thing, UnionType):
        if len(thing.items) == 2 and any(i.name == "None" for i in thing.items):
            return f"optional {_describe(thing.items[0])}"
        return " or ".join(_describe(i) for i in thing.items)
    if isinstance(thing, AnyType):
        return "a object of any type" if a else "objects of any type"

    name = thing.name.lower()
    if name == "callable":
        return (
            f"{'a ' if a else ''}callable that accepts {_describe(thing.args[0])}"
            f" and returns {_describe(thing.args[1])}"
        )
    elif name == "optional":
        return f"{'a ' if a else ''}optional {_describe(thing.args[0])}"
    elif name in {"generator", "coroutine"}:
        return (
            f"{'a ' if a else ''}{name} that yields {_describe(thing.args[0])},"
            f" sends {_describe(thing.args[1])}, returns {_describe(thing.args[2])}"
        )
    elif name == "asyncgenerator":
        return f"{'an ' if a else ''}async generator that yields {_describe(thing.args[0])}" + (
            f", sends {_describe(thing.args[1])}" if len(thing.args) > 1 else ""
        )
    elif name in {"dict", "mapping", "ordereddict", "defaultdict"}:
        return (
            f"{'a ' if a else ''}{name} with {_describe(thing.args[0])} key"
            f" and {_describe(thing.args[1])} value"
        )
    elif name in {"list", "set", "tuple", "namedtuple", "frozenset"}:
        return f"{'a ' if a else ''}{name} of {pluralize(_describe(thing.args[0], a=False))}"
    elif name == "str":
        return f"{'a ' if a else ''}string"
    elif name == "int":
        return f"{'a ' if a else ''}integer"
    elif name == "bool":
        return f"{'a ' if a else ''}boolean"
    elif name == "none":
        return "nothing"
    elif name == "any":
        return "a object of any type" if a else "objects of any type"
    elif name == "final":
        return f"{'a ' if a else ''}final {_describe(thing.args[0])}"
    elif name == "anystr":
        return f"any kind of string"
    elif name == "literal":
        return (
            f"only expressions that have literally the {'values' if len(thing.args) > 1 else 'value'}"
            f" {' or '.join(map(str, thing.args))}"
        )
    elif name == "annotated":
        return (
            f"an annotated expression with the {'values' if len(thing.args) > 1 else 'value'}"
            f" {' and '.join(map(str, thing.args))}"
        )
    elif name.startswith("supports"):
        supports_what = name[8:]
        return f"a object of that supports {supports_what}" if a else f"objects that support {supports_what}"
    else:
        return (
            ("a " + thing.name + (' ' + _describe(thing.args[0], a=False) if len(thing.args) > 0 else ""))
            if a
            else thing.name + (' ' + _describe(thing.args[0], a=False) if len(thing.args) > 0 else "")
        )


def describe(thing: Type) -> str:
    return _describe(thing).capitalize()

def _parse_def(def_):
    if isinstance(def_, AssignmentStmt):
            yield def_.type
    elif isinstance(def_, FuncDef):
        for argument in def_.arguments:
            if argument.type_annotation:
                yield argument.type_annotation
        if def_.type and def_.type.ret_type:
            yield def_.type.ret_type
    elif isinstance(def_, ClassDef):
        for thing in def_.defs.body:
            yield from _parse_def(thing)
    elif isinstance(def_, Decorator):
        yield from _parse_def(def_.func)

def parse_code(code: str) -> Generator[Type, None, None]:
    import rich
    defs = parse(code, "<function>", module=None, errors=None, options=Options()).defs
    for def_ in defs:
        yield from _parse_def(def_)

def get_json(defs):
    data = []
    for def_ in defs:
        typehint_text = str(def_).replace("?", "")
        line = def_.line
        end_line = def_.end_line
        column = def_.column + 1
        end_column = column + len(typehint_text)
        description = describe(def_)

        data.append({'typehint_text': typehint_text, 'description': description, 'line': line, 'end_line': end_line, 'column': column, 'end_column': end_column})

    return data

