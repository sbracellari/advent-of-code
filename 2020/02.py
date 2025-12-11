from util import read_file

data: list[list[str]] = [l.split(": ") for l in read_file("2020/input.txt").split("\n")]

p1: int = 0
p2: int = 0

for (policy, password) in data:
  range, c = policy.split(" ")
  r: list[int] = [int(n) for n in range.split("-")]
  if (r[0] <= password.count(c) <= r[1]): p1 += 1
  if (password[r[0]-1] == c and password[r[1]-1] != c) or (password[r[0]-1] != c and password[r[1]-1] == c): p2 +=1 

print("p1", p1)
print("p2", p2)