from util import read_file
from functools import cache

devices: dict[str, list[str]] = {
  x[0]: x[1].strip().split(" ") for x in (l.split(":") for l in read_file("2025/input/11.txt").split("\n"))}

@cache
def num_paths(start, target) -> int:
  paths: int = 0
  for output in devices[start]:
    if output == target: paths += 1
    elif output not in devices: continue
    else: paths += num_paths(output, target)
  return paths

p1: int = num_paths("you", "out")
print("p1", p1)

p2: int = num_paths("svr", "fft") * num_paths("fft", "dac") * num_paths("dac", "out")
print("p2", p2)