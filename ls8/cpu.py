"""CPU functionality."""

import sys


class CPU:
	"""Main CPU class."""

	def __init__(self):
		"""
		Construct a new CPU.
		"""
		self.ram = [0] * 256
		self.reg = [0] * 8
		self.pc = 0

	def ram_read(self, pc):
		# return value in ram at index of program step
		return self.ram[pc]

	def ram_write(self, pc):
		address = self.ram[pc + 1] # registry index
		value = self.ram[pc + 2] # registry location

		self.ram[address] = value
		print(f'Write successful {self.ram[address]}')
		self.pc += 3

	def load(self):
		"""Load a program into memory."""

		address = 0

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

		# assign to ram, not registry
		for instruction in program:
			self.ram[address] = instruction
			address += 1

	def alu(self, op, reg_a, reg_b):
		"""ALU operations."""

		if op == "ADD":
			self.reg[reg_a] += self.reg[reg_b]
		elif op == "SUB":
			self.reg[reg_a] -= self.reg[reg_b]
		elif op == "MUL":
			self.reg[reg_a] *= self.reg[reg_b]
		elif op == "DIV":
			self.reg[reg_a] /= self.reg[reg_b]
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
			print(" %02X" % self.reg[i], end='')

			print()

	def run(self, pc):
		"""Run the CPU."""
		# defining instruction
		LDI = 130
		PRN = 71
		HLT = 1
		# instruction equals current index of program counter "pc"
		# print(instruction)
		halted = False

		while not halted:
			instruction = self.ram[self.pc]

			# print(instruction)
			if instruction == HLT:
				halted = True

			elif instruction == LDI:
				self.ram_write(pc)


			elif instruction == PRN:
				value = self.ram_read(pc)

				print('prn', value)
				self.pc += 2

			else:
				print(f'Unknown instructions at index {self.pc}')
				sys.exit(1)
