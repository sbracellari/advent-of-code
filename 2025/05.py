from util import read_file

(r, ids) = read_file("2025/input/05.txt").split("\n\n")
ranges: list[tuple[int, int]] = [(int(x[0]), int(x[1])) for x in (x.split("-") for x in r.split("\n"))]
ranges.sort(key=lambda x: x[0])

p1: int = sum([1 for x in ids.split("\n") if any(r[0] <= int(x) <= r[1] for r in ranges)])
print("p1", p1)

def merge_intervals(r: list[tuple[int, int]]) -> list[tuple[int, int]]:
  count = 0
  while (count < len(r)-1):
    if (r[count][1] < r[count+1][0]): count += 1
    elif r[count][0] <= r[count+1][0] and r[count][1] >= r[count+1][1]:
      new_r: list[tuple[int, int]] = [*r[0:count], (r[count][0], r[count][1]), *r[count+2::]]
      r = new_r
    else:
      new_r: list[tuple[int, int]] = [*r[0:count], (r[count][0], r[count+1][1]), *r[count+2::]]
      r = new_r
  return r

merged_ranges: list[tuple[int, int]] = merge_intervals(ranges)
p2: int = sum([len(range(r[0], r[1]+1)) for r in merged_ranges])
print("p2", p2)