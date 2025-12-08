from util import read_file

grid: list[list[str]] = [[x for x in l] for l in read_file("2025/input/07.txt").split("\n")]

start: int = grid[0].index("S")
grid[1][start] = "|"
splits: int = 0

for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == "." and grid[i-1][j] == "|": grid[i][j] = "|"
    elif grid[i][j] == "^" and grid[i-1][j] == "|":
      grid[i][j-1], grid[i][j+1] = "|", "|"
      splits += 1

print("p1", splits)  

grid: list[list[str]] = [[x for x in l] for l in read_file("2025/input/07.txt").split("\n")]

start: int = grid[0].index("S")
grid[0][start], grid[1][start] = "1", "1"

def traverse(grid: list[list[str]]) -> None:
  for row in range(1, len(grid)):   
    if "^" not in grid[row]:
      grid[row] = grid[row-1]
      continue
    
    for char in range(1,len(grid[row])-1):
      p, c, n = grid[row][char-1], grid[row][char], grid[row][char+1]
      a, na =  grid[row-1][char], grid[row-1][char+1] 
      if grid[row][char] == "." and grid[row-1][char].isdigit(): grid[row][char] = grid[row-1][char]
      elif grid[row][char] == "^":
        grid[row][char-1] = str(int(a if a.isdigit() else 0) + int(p if p.isdigit() else 0))
        grid[row][char+1] = str(int(a if a.isdigit() else 0) + int(na if na.isdigit() else 0) + int(n if n.isdigit() else 0))
      
traverse(grid)
print("p2", sum([int(n if n.isdigit() else 0) for n in grid[-1]]))