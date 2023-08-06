import ast
from dataclasses import dataclass
from typing import Any


@dataclass
class ExprParseResult:
    lines_var: str
    eval_input: str


class ExprParseError(Exception):
    expr: str

    def __init__(self, msg, expr):
        super().__init__(msg)
        self.expr = expr


def _get_expr(parse_result: Any) -> ast.Expr | None:
    if len(parse_result.body) != 1:
        return None

    expr = parse_result.body[0]

    assert isinstance(expr, ast.Expr)
    return expr


def _eval_input_from_slice(raw_expr: str) -> ExprParseResult | None:
    lines_var = "lines"
    slice_expr = f"{lines_var}{raw_expr}"

    try:
        parse_result = ast.parse(slice_expr)
    except SyntaxError:
        return None

    expr = _get_expr(parse_result)

    if expr is None:
        return None

    if type(expr.value) != ast.Subscript:
        return None

    return ExprParseResult(
        lines_var=lines_var, eval_input=f"[l{raw_expr} for l in {lines_var}]"
    )


def _eval_input_from_func(raw_expr) -> ExprParseResult | None:
    try:
        parse_result = ast.parse(raw_expr)
    except SyntaxError:
        return None

    expr = _get_expr(parse_result)

    if expr is None:
        return None

    if not isinstance(expr.value, ast.Name):
        return None

    lines_var = "lines"
    map_expr = f"[{expr.value.id}(l) for l in {lines_var}]"
    return ExprParseResult(lines_var=lines_var, eval_input=map_expr)


def _eval_input_from_list_comp(raw_expr: str) -> ExprParseResult | None:
    try:
        parsed_expr = ast.parse(raw_expr)
    except SyntaxError:
        return None

    if len(parsed_expr.body) != 1:
        return None

    expr = parsed_expr.body[0]

    if not isinstance(expr, ast.Expr):
        return None

    raw_expr_value = expr.value
    if not isinstance(raw_expr_value, (ast.ListComp, ast.GeneratorExp)):
        return None

    assert isinstance(raw_expr_value, (ast.ListComp, ast.GeneratorExp))
    compreh = raw_expr_value
    assert isinstance(compreh.generators, list)
    assert len(compreh.generators) == 1
    generator = compreh.generators[0]  # TODO: Can have multiple generators?
    assert isinstance(generator.iter, ast.Name)
    lines_var = generator.iter.id
    assert isinstance(generator.target, ast.Name)
    return ExprParseResult(lines_var=lines_var, eval_input=raw_expr)


def parse_expr(raw_expr: str) -> ExprParseResult | None:
    # [1:2] -> [x[1:2] for x in y]
    result = _eval_input_from_slice(raw_expr)
    if result is not None:
        return result

    # [x for x in y] -> ...
    result = _eval_input_from_list_comp(raw_expr)
    if result is not None:
        return result

    # int -> [int(x) for x in y]
    result = _eval_input_from_func(raw_expr)
    if result is not None:
        return result

    # TODO:
    # str(line).split("/").join("/")
    # 1 + x
    # x + 1

    return None
