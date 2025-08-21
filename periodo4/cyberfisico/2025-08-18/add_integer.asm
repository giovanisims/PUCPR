.data 

num1 : .word 1
num2 : .word 2

.text 

# $t0-$t7 is a temporary register 

lw $t1, num1
lw $t2, num2

add $t0, $t1, $t2

li $v0, 1 # $v0 for printing, 1 to print a word

move $a0, $t0 # Assigns $t0 to $a0

syscall


