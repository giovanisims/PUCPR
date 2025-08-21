.data

newline: .asciiz "\n"
exitmessage: .asciiz "Loop has ended"

.text

main:

addi $t0, $zero, 0

while:
	bgt $t0, 10, exit
	jal printnumbers
	
	addi $t0, $t0, 1
	
	j while
exit:
	li $v0, 4
	la $a0, exitmessage
	syscall

# ----------------------- End the program 
li $v0, 10
syscall

printnumbers:
	
	li $v0, 1
	move $a0, $t0
	syscall
	
	# ----------------------- print newline
	li $v0, 4
	la $a0, newline
	syscall
	# ----------------------- 
	
	jr $ra

