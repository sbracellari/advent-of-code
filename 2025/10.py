from util import read_file
from z3 import Solver, Sum, Int, sat
from z3.z3 import ArithRef, ModelRef
from collections import deque

data: list[str] = read_file("2025/input/10.txt").split("\n")
             
def parse(data: list[str]) -> list[tuple[str, list[list[int]], list[int]]]:
  machines: list[tuple[str, list[list[int]], list[int]]] = []
  
  for parts in [m.strip().split() for m in data]:
    indicators: str = parts[0][1:-1]
    buttons: list[list[int]] = [[int(b) for b in button[1:-1].split(",")] for button in parts[1:-1]]
    joltages: list[int] = [int(v) for v in parts[-1][1:-1].split(",")]
    machines.append((indicators, buttons, joltages))
  
  return machines

machines: list[tuple[str, list[list[int]], list[int]]] = parse(data)

def press(indicators: list[str], button: list[int]) -> str:
  for n in button: indicators[n] = "#" if indicators[n] == "." else "."
  return "".join(indicators)
    
def bfs(target: str, buttons: list[list[int]]) -> int:
  visited: list[str] = []
  queue: deque[tuple[int, str]] = deque([(0, "."*len(target))])
  
  while queue:
    steps, indicators = queue.popleft()
        
    if indicators == target: return steps

    for button in buttons:
      i: str = press([c for c in indicators], button)

      if i not in visited:
        visited.append(i)
        queue.append((steps + 1, i)) 
  return 0

p1: int = 0
for machine in machines:
  p1 += bfs(machine[0], machine[1], )
  
print("p1", p1)

# this is heavily inspired by other's implementations, i didn't know how to use z3 before this
# (i still don't really)

p2: int = 0
for _, buttons, voltages in machines:
    solver = Solver()
    n: int = 0

    bvars: list[ArithRef] = [Int(f"a{n}") for n in range(len(buttons))]
    for b in bvars:
        solver.add(b >= 0)

    for i,v in enumerate(voltages):
        vvars: list[ArithRef] = [bvars[j] for j,button in enumerate(buttons) if i in button]
        solver.add(Sum(vvars) == v)

    while solver.check() == sat:
        model: ModelRef = solver.model()
        n: int = sum([model[d].as_long() for d in model]) # type: ignore
        solver.add(Sum(bvars) < n)

    p2 += n

print("p2", p2)