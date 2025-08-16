import re, sys
from typing import Any



class Interpreter:
	def __init__(self) -> None:
		self.tape: list[int]= 30000*[0]
		self.dataPointer: int=0
		
	def right(self)->int: # >
		self.dataPointer+=1
		return 0
	
	def left(self)->int: # <
		self.dataPointer-=1
		return 0
	
	def output(self)->str: # .
		return chr(self.tape[self.dataPointer]%256)


	def add(self)->int: # +
		self.tape[self.dataPointer]=(self.tape[self.dataPointer]+1)%256
		return 0
	
	def sub(self)->int: # -
		self.tape[self.dataPointer] = max(self.tape[self.dataPointer]-1,0)
		return 0
	
	def inp(self)->int: # ,
		value=ord(input())
		if value>256:
			raise ValueError("This char is not in the 256 first ascii char")
		self.tape[self.dataPointer]=value
		return 0

	


	def scrape(self,code: str) -> list[Any]:
		return re.findall(r"[+\-<>.,\[\]]", code)
	


	def command(self)-> None:
		if len(sys.argv) < 2:
			print("Usage: python MyFile.py <file.bf>")
			sys.exit(1)

		filename = sys.argv[1]

		with open(filename, "r", encoding="utf-8") as f:
			source_code = f.read()

		instructions= self.scrape(source_code)
		print(instructions)

		

