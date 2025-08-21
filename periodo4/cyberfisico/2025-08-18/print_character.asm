.data
# .data is for defining variables

character : .byte 'a'

.text
#  .text is for defining instructions

# li is for loading a 'value' into the register immediately
# $v0 is the specific register to choose the syscall code I want to run
li $v0, 11 # puts the number 11, which is the code for printing a character, into $v0

# lb loads the ASCII value from the character label
# $a0 - $a3 are registers used for arguments in a syscall or function
lb $a0, character

syscall
