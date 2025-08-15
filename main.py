import re, sys
from typing import Any

def main():

    if len(sys.argv) < 2:
        print("Usage: python MyFile.py <file.bf>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        source_code = f.read()

    instructions = scrape(source_code)
    print(instructions)

    #tape: list[int]= 30000*[0]
    #dataPointer: int=0
    #print(tape)



def output(number:int)->str:
    return chr(number%256)


def add(tape:list[int],dP:int)->int:
    tape[dP]+=1
    return 0

def scrape(code: str) -> list[Any]:
    return re.findall(r"[+\-<>.,\[\]]", code)

if __name__ == "__main__":
    main()
