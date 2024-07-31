import ttg
import sys

vars = sys.argv[1:-1]

formula = [sys.argv[-1]]

table = ((ttg.Truths(vars, formula)))

print(table.valuation())