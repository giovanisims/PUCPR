import itertools
import re
import sys
import tabulate

class Proposition:
    def __init__(self, proposition):
        self.proposition = proposition
        # Capturing variables and their negations for full evaluation
        self.variables = set(re.findall(r"[pq]", proposition))  

    @classmethod
    def get(cls):
        proposition = input("Proposição: ")
        return cls(proposition)

    @property
    def proposition(self):
        return self._proposition
    
    @proposition.setter
    def proposition(self, proposition):
        # Updated regex to handle single variables/negations and binary operations
        if re.match(r"^(~?[pq](\s*(->|\^|v|<->)\s*~?[pq])?)$", proposition):
            self.operation = re.split(r"\s*(->|\^|v|<->)\s*", proposition)
        else:
            sys.exit("Proposição inválida")
        self._proposition = proposition

class TruthTable:
    def __init__(self, proposition):
        self.proposition = proposition

    def evaluate(self, values):
        if len(self.proposition.operation) == 1:
            var = self.proposition.operation[0]
            if var.startswith('~'):
                return not values[var[1]]
            return values[var]

        op = self.proposition.operation[1]
        var1 = values[self.proposition.operation[0].strip('~')]
        if '~' in self.proposition.operation[0]:
            var1 = not var1
        var2 = values[self.proposition.operation[2].strip('~')]
        if '~' in self.proposition.operation[2]:
            var2 = not var2

        if op == "^":
            return var1 and var2
        elif op == "v":
            return var1 or var2
        elif op == "->":
            return not var1 or var2
        elif op == "<->":
            return var1 == var2
        return None

    def generate_truth_table(self):
        variables = list(self.proposition.variables) 
        combinations = itertools.product([False, True], repeat=len(variables))
        results = []
        for combo in combinations:
            values = dict(zip(variables, combo))
            result = self.evaluate(values)
            results.append((values, result))
        return results

def main():
    proposition = Proposition.get()
    truthtable = TruthTable(proposition)
    results = truthtable.generate_truth_table()
    headers = list(proposition.variables) + [proposition.proposition]
    table = [[values[var] for var in proposition.variables] + [result] for values, result in results]
    print(tabulate.tabulate(table, headers=headers, tablefmt="github"))

if __name__ == "__main__":
    main()