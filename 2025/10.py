from util import read_file
from collections import deque

machines: list[str] = read_file("2025/input/10.txt").split("\n")

def press(indicators: list[str], button: str) -> str:
  for n in button[1:-1].split(","): indicators[int(n)] = "#" if indicators[int(n)] == "." else "."
  return "".join(indicators)
    
def bfs(buttons: list[str], target: str) -> int:
  print(target, "\t", buttons)
  visited: set[str] = set()
  queue: deque[tuple[int, str]] = deque([(0, '.'*len(target))])
  
  while queue:
    steps, indicators = queue.popleft()
        
    if indicators == target: return steps

    for button in buttons:
      i: str = press([c for c in indicators], button)

      if i not in visited:
        visited.add(i)
        queue.append((steps + 1, i)) 
  return 0

p1: int = 0
for machine in machines:
  indicators, *buttons, joltage = machine.split(' ')
  p1 += bfs(buttons, indicators[1:-1])
  
print("p1", p1)