from pytruth.formula import Formula

class TruthTable():
    def __init__(self, formula):
        self.formula = formula
        self.valuations = []
        self.header = []

        self.variables = self.formula.get_variables()
        self.num_rows = 2 ** len(self.variables)

        self.header.extend(self.variables)
        self.header.append(str(self.formula))

    def compute_valuations(self):
        self._compute_valuation(0)
        self.valuations.reverse()

    def _compute_valuation(self, valuation_n):
        binary = bin(valuation_n)[2:].zfill(len(self.variables))
        valuation = {}
        valuation_list = []

        for var, val in zip(self.variables, binary):
            valuation[var] = val
            valuation_list.append(val)
        
        valuation_list.append(self.formula.evaluate(valuation))
        self.valuations.append(valuation_list)

        if valuation_n < self.num_rows - 1:
            self._compute_valuation(valuation_n + 1)

    def __str__(self):
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
