#!/usr/local/bin/python3
import argparse
import sys
from typing import Sequence, TextIO

from .expr import ExprParseError, parse_expr

HELP = """

example:

    echo 1 | %(prog)s float
    echo 5 | %(prog)s '[x for x in y if int(x) > 10]'
    echo 100 | %(prog)s '[x for x in y if int(x) > 10]'

"""


def run_cli(
    args: Sequence[str],
    stdin: TextIO = sys.stdin,
    stdout: TextIO = sys.stdout,
) -> None:
    parser = argparse.ArgumentParser(
        prog="pyq",
        epilog=HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "expr",
        help="expression to apply on each line of stdin",
    )

    parsed_args = parser.parse_args(args)
    raw_expr = parsed_args.expr

    parse_result = parse_expr(raw_expr)
    if parse_result is None:
        raise ExprParseError(f"Failed to parse expr '{raw_expr}'", expr=raw_expr)

    lines = (line.strip() for line in stdin.readlines())

    locals_ = {parse_result.lines_var: lines}
    result = eval(parse_result.eval_input, None, locals_)

    for line in result:
        stdout.write(str(line) + "\n")


if __name__ == "__main__":
    try:
        run_cli(sys.argv[1:])
    except ExprParseError as error:
        sys.stderr.write("Failed to parse expr: '%s'\n" % error.expr)
