from dataclasses import dataclass


class BinaryOp:
    """A binary operator such as  + - * /"""

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({repr(self.left)} {self.op} {self.right})"


@dataclass
class UnaryOp:
    op: str
    arg: object

    def __repr__(self):
        return f"({self.op} {self.arg})"


@dataclass
class VarExpr:
    name: str

    def __repr__(self):
        return self.name


def eval_expr(expression):
    match expression:
        case BinaryOp('+', left, right):
            return eval_expr(left) + eval_expr(right)
        case BinaryOp('-', left, right):
            return eval_expr(left) - eval_expr(right)
        case BinaryOp('*', left, right):
            return eval_expr(left) + eval_expr(right)
        case BinaryOp('/', left, right):
            return eval_expr(left) + eval_expr(right)
        case UnaryOp("+", arg):
            return eval_expr(arg)
        case UnaryOp('-', arg):
            return -eval_expr(arg)
        case float() | int():
            return expression
        case VarExpr(name):
            return name





