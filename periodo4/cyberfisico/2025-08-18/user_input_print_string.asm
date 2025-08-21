.data

prompt : .asciiz "Enter your age: " # ascii is for encoding, so use asciiz for strings

message : .ascii "\n Your age is "

.text

li $v0, 4 # 4 is for printing strings

la $a0, prompt

syscall

li $v0, 5 # 5 is for user input for an int

syscall

move $t0, $v0 # saves the user input to $t0

li $v0, 4 

la $a0, message
syscall

li $v0, 1 

move $a0, $t0

syscall