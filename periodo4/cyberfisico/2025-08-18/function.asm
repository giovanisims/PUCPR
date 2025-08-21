.data

.text

main:

addi $a1, $zero, 50
addi $a2, $zero, 100

# ---------------------------------
 
jal addnumbers

move $a0, $v0

li $v0, 1

syscall

# ---------------------------------

li $v0, 11
li $a0, 10 # this is the ascii code for newline

syscall

# ---------------------------------

jal multnumbers

move $a0, $v0

li $v0, 1

syscall

# ---------------------------------

# Always have this at the end of the main function, otherwise we get an infinite loop
li $v0, 10 
syscall

addnumbers:

add $v0, $a1, $a2 # $v0 and $v1 are function return values

jr $ra # jr is the return command and $ra the return argument

multnumbers:

mult $a1, $a2

mflo $v0

jr $ra


