.data

double : .double 3.14

.text

# need to use $f12 for floats or  doubles
l.d $f12, double # use l.s for float or l.d for double

li $v0, 3 # 3 is the code for printing a double
syscall

