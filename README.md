### Installation

```bash
pip install pylogic
```

### Example usage

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

### or

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

### , and then running

```bash
python main.py "(P -> Q)"
```
