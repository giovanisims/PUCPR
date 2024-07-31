import ttg
import sys

vars = sys.argv[1:-1]

formula = [sys.argv[-1]]


with open("auto_truth_table.txt", "a") as file:
    file.write(str(ttg.Truths(vars, formula, ints=False)) + "\n")