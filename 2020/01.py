from util import read_file

nums: list[int] = [int(n) for n in read_file("2020/input.txt").split("\n")]

product_2: int = [a*b for a in nums for b in nums if a+b == 2020][0]
print("p1", product_2)

product_3: int = [a*b*c for a in nums for b in nums for c in nums if a+b+c == 2020][0]
print("p2", product_3)