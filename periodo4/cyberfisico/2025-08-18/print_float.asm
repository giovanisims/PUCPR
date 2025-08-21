.data

float : .float 3.14

.text

# need to use $f12 for floats or  doubles
l.s $f12, float # use l.s for float or l.d for double

li $v0, 2 # 2 is the code for printing a float
syscall

