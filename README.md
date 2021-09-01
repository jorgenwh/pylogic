This is very much a work in project, and it will probably never be finished.
It only implements a helpful tool for a very small part of the course IN1150 at UiO.

## Installation

```bash
pip install pylogic
```

## Example usage

#### script1.py

```python
from pylogic.propositional import Formula, TruthTable

expr = "((P or Q) -> (P and Q))"
formula = Formula(expr)
truth_table = TruthTable(formula)

print(f"Formula: {formula}")
print(f"Variables: {formula.get_variables()}")

print("\nTruth table:")
print(truth_table)
```

#### and then running by
```bash
python script1.py
```

#### or, 
#### script2.py

```python
from pylogic.propositional import Formula, TruthTable
import sys

expr = sys.argv[1]
formula = Formula(expr)
truth_table = TruthTable(formula)

print(f"Formula: {formula}")
print(f"Variables: {formula.get_variables()}")

print("\nTruth table:")
print(truth_table)
```

#### and then running by

```bash
python script2.py "((P or Q) -> (P and Q))"
```

#### Both will yield the same output:

```
Formula: ((P or Q) -> (P and Q))
Variables: ['P', 'Q']

Truth table:
+---+---+-------------------------+
| P | Q | ((P or Q) -> (P and Q)) |
+---+---+-------------------------+
| 1 | 1 |            1            |
+---+---+-------------------------+
| 1 | 0 |            0            |
+---+---+-------------------------+
| 0 | 1 |            0            |
+---+---+-------------------------+
| 0 | 0 |            1            |
+---+---+-------------------------+
```
