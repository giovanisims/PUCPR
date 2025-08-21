.data

diff: .asciiz "The numbers are different"
equal: .asciiz "The numbers are equal"

.text

main:

addi $t0, $zero, 5 
addi $t1, $zero, 6

bne $t0, $t1, numbersdiff

# -------------------------------- if the numbers are equal

li $v0, 4
la $a0, equal

syscall

# ------------------------------------
li $v0, 10 
syscall

numbersdiff:

li $v0, 4
la $a0, diff

syscall

