from typing import List
from pylogic.misc import count_parentheses, ParenthesesError

class Valuation(dict):
    def __init__(self, valuation: dict = {}):
        self.valuation = valuation
        self.variables = set(valuation.keys())

    def __str__(self) -> str:
        s = ""
        for var in self.variables:
            s += var + ": " + str(self.valuation[var]) + ", "
        if len(self.variables) != 0:
            s = s[:-2]
        return "Valuation(" + s + ")"

class _FormulaBase():
    def __init__(self):
        self.sub_formulae = []
        self.variables = []
        self.type = None

    def evaluate(self, valuation: Valuation) -> int:
        if self.type in ["-", "and", "or", "->"]:
            truth_values = [f.evaluate(valuation) for f in self.sub_formulae]
            if self.type == "-" and sum(truth_values) == 0:
                return 1
            if self.type == "and" and sum(truth_values) == 2:
                return 1
            if self.type == "or" and sum(truth_values) >= 1:
                return 1
            if self.type == "->" and not (truth_values[0] == 1 and truth_values[1] == 0):
                return 1
            return 0
        else:
            return int(valuation[self.variables[0]])

    def get_variables(self) -> List[str]:
        return self.variables

    def __str__(self) -> str:
        if self.type in ["and", "or", "->"]:
            return f"({str(self.sub_formulae[0])} {self.type} {str(self.sub_formulae[1])})"
        if self.type == "-":
            return f"-{str(self.sub_formulae[0])}"
        return self.variables[0]

class Formula():
    def __init__(self, expr: str):
        if not count_parentheses(expr):
            raise ParenthesesError("Parentheses mismatch: number of left and right parentheses are not equal.")
        parser = _FormulaParser()
        self.base = parser.parse(expr)

    def evaluate(self, valuation: Valuation) -> int:
        return self.base.evaluate(valuation)

    def get_variables(self) -> List[str]:
        return self.base.get_variables()

    def __str__(self) -> str:
        return str(self.base)

class _FormulaParser():
    def __init__(self):
        self.idx = 0
        self.string = None
        self.formula = None

    def parse(self, string: str) -> _FormulaBase:
        self.string = string
        self.skip_whites()
        self.formula = self.parse_sub()
        assert len(self.formula.get_variables()) > 0

        self.formula.variables = list(set(self.formula.variables))
        self.formula.variables.sort()
        return self.formula

    def parse_sub(self) -> _FormulaBase:
        if self.string[self.idx] == "(":
            return self.parse_aop()
        elif self.string[self.idx] == "-":
            return self.parse_neg()
        else:
            return self.parse_var()

    def parse_aop(self) -> _FormulaBase:
        assert self.string[self.idx] == "("
        self.idx += 1

        formula = _FormulaBase()
        sub_formula1 = self.parse_sub()
        self.skip_whites()
        formula.type = self.parse_sign()
        self.skip_whites()
        sub_formula2 = self.parse_sub()

        formula.sub_formulae.append(sub_formula1)
        formula.sub_formulae.append(sub_formula2)
        formula.variables.extend(sub_formula1.variables)
        formula.variables.extend(sub_formula2.variables)

        self.skip_whites()
        assert self.string[self.idx] == ")"
        self.idx += 1

        formula.variables = list(set(formula.variables))
        formula.variables.sort()
        return formula

    def parse_neg(self) -> _FormulaBase:
        assert self.string[self.idx] == "-"
        self.idx += 1
        
        formula = _FormulaBase()
        formula.type = "-"
        sub_formula = self.parse_sub()

        formula.sub_formulae.append(sub_formula)
        formula.variables.extend(sub_formula.variables)
        self.skip_whites()

        formula.variables = list(set(formula.variables))
        formula.variables.sort()
        return formula
        
    def parse_var(self) -> _FormulaBase:
        formula = _FormulaBase()
        formula.type = "var" 
        formula.variables.append(self.string[self.idx])
        self.idx += 1
        return formula

    def parse_sign(self) -> str:
        sign = ""
        while self.string[self.idx] != " ":
            sign += self.string[self.idx]
            self.idx += 1
        return sign

    def skip_whites(self) -> None:
        while self.idx < len(self.string) and self.string[self.idx] == " ":
            self.idx += 1

class TruthTable():
    def __init__(self, formula):
        self.formula = formula.base
        self.valuations = []
        self.header = []

        self.variables = self.formula.get_variables()
        self.num_rows = 2 ** len(self.variables)

        self.header.extend(self.variables)
        self.header.append(str(self.formula))

        self._compute_valuation(0)
        self.valuations.reverse()

    def _compute_valuation(self, valuation_n) -> None:
        binary = bin(valuation_n)[2:].zfill(len(self.variables))
        valuation = Valuation()
        valuation_list = []

        for var, val in zip(self.variables, binary):
            valuation[var] = val
            valuation_list.append(val)
        
        valuation_list.append(self.formula.evaluate(valuation))
        self.valuations.append(valuation_list)

        if valuation_n < self.num_rows - 1:
            self._compute_valuation(valuation_n + 1)

    def __str__(self) -> str:
        f_len = len(str(self.formula))
        sep = "+---" * len(self.variables) + "+--"
        for i in range(f_len + 1):
            sep += "+\n" if i == f_len else "-"
        s = sep

        for var in self.variables:
            s += "| " + var + " "
        s += "| " + str(self.formula) + " |\n" + sep
        
        for valuation in self.valuations:
            for i, val in enumerate(valuation):
                if i == len(valuation) - 1:
                    l = int(f_len / 2)
                    s += "|" + (" " if f_len % 2 == 1 else "") + (" " * l) + str(val) + (" " * l) + " |"
                else:
                    s += "| " + str(val) + " "
            s += "\n" + sep

        return s
