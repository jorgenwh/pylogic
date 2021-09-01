from pylogic.propositional import Formula, Valuation, TruthTable
import sys

if __name__ == "__main__":
    expr = "((P or Q) -> (P and Q))"
    formula = Formula(expr)
    truth_table = TruthTable(formula)

    print(f"Formula: {formula}")
    print(f"Variables: {formula.get_variables()}")
    
    print("\nTruth table:")
    print(truth_table)
