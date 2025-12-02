from util import read_file

data: list[tuple[str, int]] = [(l[0], -int(l[1::]) if l[0] == "L" else int(l[1::])) for l in read_file("2025/input/01.txt").split("\n")]

p1: int = [pos:= 50, [1 if (pos := ((pos + amount) % 100)) == 0 else 0 for (_, amount) in data]][1].count(1)
print("p1", p1)

pos: int = 50
p2: int = 0
for (direction, amount) in data:
  q, r = divmod(pos + amount, 100)
  p2 += abs(q)
  
  if (pos == 0 and direction == "L"): p2 -= 1
  if (pos > 0 and direction == "L" and r == 0): p2 += 1
  
  pos = r
  
print("p2", p2)