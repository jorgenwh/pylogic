class _ValuationBase(dict):
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
