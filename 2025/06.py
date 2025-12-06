from util import read_file

p1_rows: list[list[str]]= [x.split() for x in read_file("2025/input/06.txt").split("\n")]
p1_transposed: list[list[str]] = list(map(list, zip(*p1_rows)))

p1: int = 0
for t in p1_transposed:
  nums: list[str] =  t[0:-1]
  op: str = t[-1]
  if op == "+": p1 += sum([int(n) for n in nums])
  else: 
    res: int = 1
    for n in nums: res *= int(n) # type: ignore
    p1 += res

print("p1", p1)

p2_rows: list[str] = read_file("2025/input/06.txt").split("\n")
p2_transposed: list[list[str]] = list(map(list, zip(*p2_rows)))
p2_transposed_new: list[str] = ["".join(t).strip() for t in p2_transposed]
groups: list[list[str]] = []

group: list[str] = []
for i in range(len(p2_transposed_new)):
  if p2_transposed_new[i] == "":
    groups.append(group)
    group = []
    continue
  else: group.append(p2_transposed_new[i])
  
  if i == len(p2_transposed_new) - 1: groups.append(group)
    
p2 = 0
for g in groups:
  op: str = "" 
  n: list[int] = []
  for s in g:
    if "*" in s or "+" in s: op, n = s[-1], [*n, int(s[0:-1])]
    elif s != "": n.append(int(s)) 
  if op == "+": p2 += sum(n)
  else: 
    res = 1
    for x in n: res *= x
    p2 += res

print("p2", p2)