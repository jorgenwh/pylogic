import sys
from pytruth.formula_parser import FormulaParser
from pytruth.formula import Formula
from pytruth.truth_table import TruthTable

def count_parentheses(expr):
    """
    Makes sure the number of left and right parentheses are the same.
    """
    if expr.count("(") != expr.count(")"):
        print("Invalid formula: input formula must have an equal number of open and close parentheses.")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid run: no input formula specified")
        exit(1)

    # ensure parentheses count is correct
    count_parentheses(sys.argv[1])

    parser = FormulaParser()
    formula = parser.parse(sys.argv[1]) 
    print(f"Input formula: {formula}")
    print(f"Variables: {formula.get_variables()}")

    truth_table = TruthTable(formula)
    truth_table.compute_valuations()
    print("\nTruth table:")
    print(truth_table)

