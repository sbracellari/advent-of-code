from util import read_file, distance
import itertools
import time

start_time: float = time.time()

coords: list[list[int]] = [[int(x) for x in l.split(",")] for l in read_file("2025/input/08.txt").split("\n")]

def calc_distances(coords: list[list[int]]) -> dict[tuple[int, int], float]:
  distances: dict[tuple[int, int], float] = {}

  for c in range(len(coords)-1):
    for j in range(c+1, len(coords)):
      distances[(c, j)] = distance(coords[c], coords[j])
  
  return {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

def construct_individual_circuit(p: tuple[int, int], circuits: list[list[int]]) -> list[list[int]]:
  if len(circuits) == 0:
    circuits.append([*p])
    return circuits
    
  for c in range(len(circuits)):
    if p[0] in circuits[c] and p[1] in circuits[c]:
      break
    elif (p[0] in circuits[c] and p[1] not in circuits[c]) or (p[0] not in circuits[c] and p[1] in circuits[c]):
      circuits[c].extend(p)
      circuits[c] = list(set(circuits[c]))
      break
    elif p[0] not in circuits[c] and p[1] not in circuits[c] and c == len(circuits)-1:
      circuits.append([*p])

  return merge_circuits(circuits)

def construct_final_circuits(num_pairs: int, distances: dict[tuple[int, int], float]) -> list[list[int]]:
  circuits: list[list[int]] = []
  
  for i in range(num_pairs):
    p: tuple[int, int] = list(distances.keys())[i]
    circuits = construct_individual_circuit(p, circuits)
    if len(circuits[0]) == len(coords): 
      print("p2", coords[p[0]][0] * coords[p[1]][0])
      break
      
  return circuits

def merge_circuits(circuits: list[list[int]]) -> list[list[int]]:
  circuit_set: set[int] = set(itertools.chain.from_iterable(circuits)) 

  for c in circuit_set:
    elements: list[list[int]] = [circuit for circuit in circuits if c in circuit]
    for i in elements:
      circuits.remove(i)
    circuits += [list(set(itertools.chain.from_iterable(elements)))]
  
  circuits.sort(key=lambda x: len(x), reverse=True)
  return circuits

def run(part: int) -> None:
  distances: dict[tuple[int, int], float] = calc_distances(coords)
  circuits: list[list[int]] = construct_final_circuits(1000 if part == 1 else len(distances), distances)
  if part == 1: print("p1", len(circuits[0])*len(circuits[1]*len(circuits[2])))

run(2)

print("--- %s seconds ---" % (time.time() - start_time))