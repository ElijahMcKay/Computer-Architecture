import sys

# General overview
# 1. Go into memory
# 2. Grab an instruction out
# 3. LS-8 spec says exactly what to do with that instruction
# 4. Execute that
# ex.  print out number with PRN instruction
# ex. in project, LDI = SAVE_REG


PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4

memory = [
	PRINT_BEEJ,
	# this SAVE_REG instruction is 3 indexes long in the array
	SAVE_REG, # SAVE_REGE value 10 in R2
	20, # value 10 #ARGUMENTS ARE CALLED OPERANDS IN ASSEMBLY LANGUAGE
	2, # R2
	PRINT_REG, # PRINT_REG R2
	2,
	HALT,
]

# -------------
# print("beej!")
# r2 = 10
# print(r2)
# -------------

register = [0] * 8 # Like variables, fixed number of them, fixed names R0, R1, R2... R7

# program counter is current index, or pointer to currently executed instruction
pc = 0
halted = False

while not halted:
	instruction = memory[pc]

	if instruction == PRINT_BEEJ:
		print('Beej')
		pc += 1

	elif instruction == SAVE_REG:
		value = memory[pc + 1] # 1 index after current instruction (operand)
		reg_num = memory[pc + 2] # 2 index after current instruction (operand)

		register[reg_num] = value
		pc += 3


	elif instruction == PRINT_REG:
		reg_num = memory[pc + 1]

		print(register[reg_num])
		pc += 2

	elif instruction == HALT:
		halted = True

	else:
		print('unknown')
		sys.exit(1)

