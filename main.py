import sys
from pylogic.propositional import Formula, TruthTable

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid run: no input formula specified")
        exit(1)

    formula = Formula(sys.argv[1])
    print(f"Input formula: {formula}")
    print(f"Variables: {formula.get_variables()}")

    truth_table = TruthTable(formula)
    print("\nTruth table")
    print(truth_table)
