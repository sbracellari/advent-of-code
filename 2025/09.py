from util import read_file
from collections import deque
from itertools import combinations

coords: list[tuple[int, int]] = [
  (int(x[1]), int(x[0])) for x in (l.split(",") for l in read_file("2025/input/09.txt").split("\n"))]

x: list[int] = sorted(list(set(list(map(lambda c: c[1], coords)))))
x_map: dict[int, int] = {x: i for i, x in enumerate(x)}

y: list[int] = sorted(list(set(list(map(lambda c: c[0], coords)))))
y_map: dict[int, int] = {y: i for i, y in enumerate(y)}

grid: list[list[str]] = [["."]*len(x) for _ in range(len(y))]

for c in coords: grid[y_map[c[0]]][x_map[c[1]]] = "#"
vertices: list[tuple[int, int]] = [(y_map[c[0]], x_map[c[1]]) for c in coords]

for i in range(len(vertices)):
  c1: tuple[int, int] = vertices[i]
  c2: tuple[int, int] = vertices[(i + 1) % len(vertices)]

  if c1[1] == c2[1]:
    for r in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1): grid[r][c1[1]] = '#'
  elif c1[0] == c2[0]:
    for r in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1): grid[c1[0]][r] = '#'

def flood_fill(img: list[list[str]], sc: int, sr: int, new_color: str) -> list[list[str]]:
  if img[sc][sr] == new_color: return img

  num_visited: int = 0
  directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  q: deque[tuple[int, int]] = deque()
  old_color: str = img[sc][sr]
  q.append((sc, sr))

  img[sc][sr] = new_color

  while q:
    y, x = q.popleft()

    for dy, dx in directions:
      nx: int = x + dx
      ny: int = y + dy

      if 0 <= ny < len(img) and 0 <= nx < len(img[0]) and img[ny][nx] == old_color:
        img[ny][nx] = new_color
        num_visited += 1
        q.append((ny, nx))

  return img

grid = flood_fill(grid, 100, 100, "#")

def is_enclosed(a: tuple[int, int], b: tuple[int, int], grid: list[list[str]]) -> bool:
  x1, x2 = sorted([x_map[a[1]], x_map[b[1]]])
  y1, y2 = sorted([y_map[a[0]], y_map[b[0]]])

  for x in range(x1, x2 + 1):
    if grid[y1][x] == '.' or grid[y2][x] == '.': return False

  for y in range(y1, y2 + 1):
    if grid[y][x1] == '.' or grid[y][x2] == '.': return False
  return True

p1: int = 0
p2: int = 0

for a, b in combinations(coords, 2):
  area = (abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1)
  if (is_enclosed(a, b, grid)) and area > p2: p2 = area
  elif area > p1: p1 = area

print("p1", p1)
print("p2", p2)