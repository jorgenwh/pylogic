class Formula():
    def __init__(self):
        self.subformulae = []
        self.variables = []
        self.type = None

    def evaluate(self, valuation):
        if self.type in ["-", "and", "or", "->"]:
            truth_values = [f.evaluate(valuation) for f in self.subformulae]
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

    def get_variables(self):
        return self.variables

    def __str__(self):
        if self.type in ["and", "or", "->"]:
            return f"({str(self.subformulae[0])} {self.type} {str(self.subformulae[1])})"
        if self.type == "-":
            return f"-{str(self.subformulae[0])}"
        return self.variables[0]
