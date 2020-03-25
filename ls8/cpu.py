"""CPU functionality."""

import sys

LDI = 130
PRN = 71
HLT = 1

class CPU:
	"""Main CPU class."""

	def __init__(self):
		"""
		Construct a new CPU.
		"""
		self.ram = [0] * 256
		self.register = [0] * 8
		self.pc = 0

	# accepts address to read, returns value at that index
	def ram_read(self, MAR):
		# return value in ram at index of program step
		return self.ram[MAR]

	# accepts a value (MDR) and an address (MAR) to write it to
	def ram_write(self, MAR, MDR):
		self.ram[MAR] = MDR

	# takes file input
	def load(self):
		"""Load a program into memory."""
		# For now, we've just hardcoded a program:

		program = [
				# From print8.ls8
						0b10000010,  # LDI R0,8
						0b00000000, # index in registry, not RAM
						0b00001000, # value
						0b01000111,  # PRN R0
						0b00000000,
						0b00000001,  # HLT
			]

		address = 0


		for instruction in program:
			self.ram[address] = instruction
			address += 1

	def alu(self, op, reg_a, reg_b):
		"""ALU operations."""

		if op == "ADD":
			self.register[reg_a] += self.register[reg_b]
		elif op == "SUB":
			self.register[reg_a] -= self.register[reg_b]
		elif op == "MUL":
			self.register[reg_a] *= self.register[reg_b]
		elif op == "DIV":
			self.register[reg_a] /= self.register[reg_b]
		else:
			raise Exception("Unsupported ALU operation")

	def trace(self):
		"""
		Handy function to print out the CPU state. You might want to call this
		from run() if you need help debugging.
		"""

		print(f"TRACE: %02X | %02X %02X %02X |" % (
				self.pc,
				#self.fl,
				#self.ie,
				self.ram_read(self.pc),
				self.ram_read(self.pc + 1),
				self.ram_read(self.pc + 2)
			), end='')

		for i in range(8):
			print(" %02X" % self.register[i], end='')

			print()

	def run(self):
		"""Run the CPU."""
		# defining instruction
		# instruction equals current index of program counter "pc"
		# print(instruction)
		halted = False

		while not halted:
			instruction = self.ram[self.pc]
			operand_a = self.ram_read(self.pc + 1)
			operand_b = self.ram_read(self.pc + 2)

			# print(instruction)
			if instruction == HLT:
				halted = True

			# 3 steps to an LDI
			# Step 1: reading instruction
			elif instruction == LDI:
				# Step 2: location		# Step 3: value
				self.register[operand_a] = operand_b
				self.pc += 3

			elif instruction == PRN:
				value = self.register[operand_a]
				print(value)
				self.pc += 2

			else:
				print(f'Unknown instructions at index {self.pc}')
				sys.exit(1)
