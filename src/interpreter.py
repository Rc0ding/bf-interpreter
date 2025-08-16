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
		self.jump = self.build_bracket_map(self.code)  
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
		ip = self.instructionPointer
		while ip < len(self.code):
			cmd = self.code[ip]

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
					ip = self.jump[ip]  

			elif cmd == ']':
		
				if self.tape[self.dataPointer] != 0:
					ip = self.jump[ip]  

		
			ip += 1

			self.instructionPointer = ip  
		
	


	def build_bracket_map(self, code: list[Any]) -> dict[int, int]:
		stack: list[int] = []
		jump: dict[int, int] = {}
		for i, c in enumerate(code):
			if c == '[':
				stack.append(i)
			elif c == ']':
				if not stack:
					raise SyntaxError(f"Unmatched ']' at position {i}")
				j = stack.pop()
				jump[i] = j
				jump[j] = i
		if stack:

			raise SyntaxError(f"Unmatched '[' at position {stack[-1]}")
		return jump
	
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
		

