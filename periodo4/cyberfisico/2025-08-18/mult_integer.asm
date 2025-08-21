.data

.text

addi $t1, $zero, 5 # addi adds two registers and a constant, here $t1 is holding 5 because we add 0 + 5, good for fully temp registers
addi $t2, $zero, 10

mult $t1, $t2

mflo $a0 # use this to put the lo results of the multiplication, in a register

li $v0, 1

syscall