## Installation

```bash
pip install pylogic
```

## Example usage

### script1.py

```python
from pylogic.propositional import Formula, TruthTable

expr = "(P -> Q)"
formula = Formula(expr)
truth_table = TruthTable(formula)

print(f"Formula: {formula}")
print(f"Variables: {formula.get_variables()}")

print("\nTruth table:")
print(truth_table)
```

### script2.py

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

### , and then running one of the following

```bash
python script1.py
python script2.py "(P -> Q)"
```
