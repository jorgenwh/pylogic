from pytruth.formula import Formula

class FormulaParser():
    def __init__(self):
        self.idx = 0
        self.string = None
        self.formula = None

    def parse(self, string):
        self.string = string
        self.skip_whites()
        self.formula = self.parse_sub()
        assert len(self.formula.get_variables()) > 0

        self.formula.variables = list(set(self.formula.variables))
        self.formula.variables.sort()
        return self.formula

    def parse_sub(self):
        if self.string[self.idx] == "(":
            return self.parse_aop()
        elif self.string[self.idx] == "-":
            return self.parse_neg()
        else:
            return self.parse_var()

    def parse_aop(self):
        assert self.string[self.idx] == "("
        self.idx += 1

        f = Formula()
        sub1 = None
        sub2 = None
        
        sub1 = self.parse_sub()

        self.skip_whites()
        f.type = self.parse_sign()
        self.skip_whites()

        sub2 = self.parse_sub()

        f.subformulae.append(sub1)
        f.subformulae.append(sub2)
        f.variables.extend(sub1.variables)
        f.variables.extend(sub2.variables)

        self.skip_whites()
        assert self.string[self.idx] == ")"
        self.idx += 1

        f.variables = list(set(f.variables))
        f.variables.sort()
        return f

    def parse_neg(self):
        assert self.string[self.idx] == "-"
        self.idx += 1
        
        f = Formula()
        f.type = "-"
        sub = self.parse_sub()

        f.subformulae.append(sub)
        f.variables.extend(sub.variables)
        self.skip_whites()

        f.variables = list(set(f.variables))
        f.variables.sort()
        return f
        
    def parse_var(self):
        f = Formula()
        f.type = "var"
        f.variables.append(self.string[self.idx])
        self.idx += 1
        return f

    def parse_sign(self):
        sign = ""
        while self.string[self.idx] != " ":
            sign += self.string[self.idx]
            self.idx += 1
        return sign

    def skip_whites(self):
        while self.idx < len(self.string) and self.string[self.idx] == " ":
            self.idx += 1
