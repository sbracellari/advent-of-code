from util import read_file

grid: list[list[str]] = [[c for c in row] for row in read_file("2025/input/04.txt").split("\n")]
positions: list[tuple[int, int]] = [(-1, 0),(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def find_rolls(grid: list[list[str]], count: int, locs: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], int]:
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      if grid[i][j] == "@":
        surroundings: int = sum([0 if i+y < 0 or i+y >= len(grid) or j+x < 0 or j+x >= len(grid[i]) or grid[i+y][x+j] == "." else 1 for (y, x) in positions])
        if (surroundings < 4):
          locs.append((i, j))
          count += 1 
  return locs, count

def remove_rolls(grid) -> int:
  count: int = 0

  while (True):
    locs, count = find_rolls(grid, count, [])
    if len(locs) == 0: break
    for (y, x) in locs: grid[y][x] = "."
    
  return count

_, count = find_rolls(grid, 0, [])
print("p1", count)
       
count: int = remove_rolls(grid)
print("p2", count)