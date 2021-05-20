import sys
from formula_parser import FormulaParser
from formula import Formula
from truth_table import TruthTable

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid run: no input formula specified")

    parser = FormulaParser()
    formula = parser.parse(sys.argv[1]) 
    print(f"Input formula: {formula}")
    print(f"Variables: {formula.get_variables()}")

    truth_table = TruthTable(formula)
    truth_table.compute_valuations()
    print("\nTruth table:")
    print(truth_table)

