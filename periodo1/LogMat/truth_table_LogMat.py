import ttg
import sys

vars = sys.argv[1:-1]

formula = [sys.argv[-1]]

print((str(ttg.Truths(vars, formula, ints=False))))