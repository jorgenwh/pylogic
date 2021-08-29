class ParenthesesError(Exception):
    pass

def count_parentheses(expr: str) -> bool:
    """
    Counts the number of left and right parentheses in an expression.

    Args:
        expr (str): the expression string.
    Returns:
        (bool): True if the expression string has an equal number of left and right
            parentheses, or False otherwise.
    """
    return expr.count("(") == expr.count(")")
