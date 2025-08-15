import re, sys
from typing import Any



class Interpreter:
	def __init__(self) -> None:
		self.tape: list[int]= 30000*[0]
		self.dataPointer: int=0
		


	def output(self,number:int)->str:
		return chr(number%256)


	def add(self,tape:list[int],dP:int)->int:
		tape[dP]+=1
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

		

