def read_file(path: str) -> str:
  with open(path, "r") as file:
    data: str = file.read()
    return data

def distance(a: list[int], b: list[int]) -> int:
  return (b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2