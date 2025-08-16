import re, sys
from typing import Any

class Interpreter:
	def __init__(self) -> None:
		self.code = self.command()           
		self.jump = self.build_bracket_map(self.code)
		self.tape: list[int] = [0] * 30000
		self.dataPointer: int = 0
		self.instructionPointer: int = 0
		self.run()


	def run(self) -> None:
		code = self.code
		jump = self.jump
		tape = self.tape
		dp = self.dataPointer
		ip = self.instructionPointer
		n = len(code)

		read_byte = sys.stdin.buffer.read 
		out_chunks:list[Any] = []
		CHUNK = 128
		write = sys.stdout.write

		while ip < n:
			c = code[ip]

			if c == '>':
				dp += 1
				if dp >= len(tape):
					tape.append(0)

			elif c == '<':
				if dp == 0:
					raise IndexError("Data pointer moved left of cell 0")
				dp -= 1

			elif c == '+':
				tape[dp] = (tape[dp] + 1) & 0xFF

			elif c == '-':
				tape[dp] = (tape[dp] - 1) & 0xFF

			elif c == '.':
				out_chunks.append(chr(tape[dp]))
				if len(out_chunks) >= CHUNK:
					write(''.join(out_chunks))
					out_chunks.clear()

			elif c == ',':
				b = read_byte(1)
				if not b:         
					tape[dp] = 0
				else:
					tape[dp] = b[0]

			elif c == '[':
				if tape[dp] == 0:
					ip = jump[ip]  

			elif c == ']':
				if tape[dp] != 0:
					ip = jump[ip]  

			ip += 1

		# flush any buffered output once
		if out_chunks:
			write(''.join(out_chunks))

		# sync back
		self.dataPointer = dp
		self.instructionPointer = ip
		self.tape = tape


	def build_bracket_map(self, code: str) -> dict[int, int]:
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

	def scrape(self, code: str) -> str:

		return ''.join(re.findall(r"[+\-<>.,\[\]]", code))

	def command(self) -> str:
		if len(sys.argv) < 2:
			print("Usage: python MyFile.py <file.bf>")
			sys.exit(1)
		filename = sys.argv[1]
		with open(filename, "r", encoding="utf-8") as f:
			source_code = f.read()
		return self.scrape(source_code)
