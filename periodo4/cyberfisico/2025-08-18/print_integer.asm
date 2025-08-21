.data

number : .word 100

.text

li $v0, 1 # 1 is the code for printing an integer

lw $a0, number # since its a word we use load word

syscall