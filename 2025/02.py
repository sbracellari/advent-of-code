from util import read_file

data: list[list[str]] = [l.split("-") for l in read_file("2025/input/02.txt").split(",")]

def is_valid_id(x: int, p: int) -> bool: 
  s: str = str(x)
  l: int = len(s)
  
  return (l % 2 == 1 or s[0:l//2] != s[l//2::]) if p == 1 else s not in (s + s)[1:-1] 

part = 2
p: int = sum([sum([x for x in range(int(n[0]), int(n[1])+1) if not is_valid_id(x, part)]) for n in data])

print("p{part} {p}".format(part = part, p = p))