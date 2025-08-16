import re, sys
from typing import Any



class Interpreter:

	def __init__(self) -> None:
		self.code= self.command()
		print("test")
		self.tape: list[int]= 30000*[0]
		self.dataPointer: int= 0
		self.instructionPointer: int = 0
		self.loop_value: int = 0
		self.run()
	


	def right(self) -> int:  # >
		self.dataPointer += 1
		if self.dataPointer >= len(self.tape):
			self.tape.append(0)  # grow tape to the right if needed
		return 0

	def left(self) -> int:  # <
		if self.dataPointer == 0:
			raise IndexError("Data pointer moved left of cell 0")
		self.dataPointer -= 1
		return 0
	
	def output(self)->str: # .
		return chr(self.tape[self.dataPointer]%256)


	def add(self)->int: # +
		self.tape[self.dataPointer]=(self.tape[self.dataPointer]+1)%256
		return 0
	
	def sub(self)->int: # -
		self.tape[self.dataPointer]=(self.tape[self.dataPointer]-1)%256
		return 0
	
	
	def inp(self) -> int:  # ,
		s = input()
		ch = s[0] if s else "\n"           # tolerate empty line
		self.tape[self.dataPointer] = ord(ch) & 0xFF
		return 0

	
	def run(self)-> None: # []
		
		while self.instructionPointer < len(self.code):
			cmd = self.code[self.instructionPointer]

			if cmd == '>':
				self.right()
			elif cmd == '<':
				self.left()
			elif cmd == '+':
				self.add()
			elif cmd == '-':
				self.sub()
			elif cmd == '.':
				print(self.output(),end="")
			elif cmd == ',':
				self.inp()
			elif cmd == '[':
				if self.tape[self.dataPointer] == 0:
					self.loop_value = 1
				while self.loop_value > 0:
					self.instructionPointer += 1
					if self.code[self.instructionPointer] == '[':
						self.loop_value += 1
					elif self.code[self.instructionPointer] == ']':
						self.loop_value -= 1

			elif cmd == ']':
				close_brackets=0
				if self.tape[self.dataPointer] != 0:
				# jump back to after matching [
					close_brackets = 1
				while close_brackets > 0:
					self.instructionPointer -= 1
					if self.code[self.instructionPointer] == ']':
						close_brackets += 1
					elif self.code[self.instructionPointer] == '[':
						close_brackets -= 1
			# move to next instruction
			self.instructionPointer += 1
		
	def scrape(self,code: str) -> list[Any]:
		return re.findall(r"[+\-<>.,\[\]]", code)
	


	def command(self)-> list[Any]:
		if len(sys.argv) < 2:
			print("Usage: python MyFile.py <file.bf>")
			sys.exit(1)

		filename = sys.argv[1]

		with open(filename, "r", encoding="utf-8") as f:
			source_code = f.read()

		instructions= self.scrape(source_code)
		return instructions
		

