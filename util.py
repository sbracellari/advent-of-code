def read_file(path: str) -> str:
  with open(path, "r") as file:
    data: str = file.read()
    return data