from util import read_file

banks: list[str] = read_file("2025/input/03.txt").split("\n")

def find_largest_num(x: str, jolts: str, num_length: int, digit: int) -> int:
  if digit == -1 or num_length == 0: return int(jolts)
  
  i: int = x.find(str(digit))
  if i == -1 or i > len(x) - num_length: return find_largest_num(x, jolts, num_length, digit - 1)
  else: return find_largest_num(x[i+1::], jolts + x[i], num_length-1, 9)

joltage: int = sum([find_largest_num(bank, "", 12, 9) for bank in banks])  
print("p2", joltage)