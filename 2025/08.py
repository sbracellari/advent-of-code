from util import read_file
from math import dist

coords: list[list[int]] = [[int(x) for x in l.split(",")] for l in read_file("2025/input/08.txt").split("\n")]

def calc_distances(coords: list[list[int]]) -> dict[tuple[int, int], float]:
  distances: dict[tuple[int, int], float] = {}

  for c1 in range(len(coords)-1):
    for c2 in range(c1+1, len(coords)):
      distances[(c1, c2)] = dist(coords[c1], coords[c2])
  
  return {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

def construct_circuit(p: tuple[int, int], circuits: list[list[int]]) -> list[list[int]]:
  if len(circuits) == 0:
    circuits.append([*p])
    return circuits
    
  for c in range(len(circuits)):
    if p[0] in circuits[c] and p[1] in circuits[c]: break
    elif p[0] not in circuits[c] and p[1] not in circuits[c] and c == len(circuits)-1: circuits.append([*p])
    elif (p[0] in circuits[c] and p[1] not in circuits[c]) or (p[0] not in circuits[c] and p[1] in circuits[c]):
      circuits[c].extend(p)
      circuits[c] = list(set(circuits[c]))
      break

  return merge_circuits(circuits)

def final_circuits(num_pairs: int, distances: dict[tuple[int, int], float]) -> list[list[int]]:
  circuits: list[list[int]] = []
  
  for i in range(num_pairs):
    p: tuple[int, int] = list(distances.keys())[i]
    circuits = construct_circuit(p, circuits)
    if len(circuits[0]) == len(coords): 
      print("p2", coords[p[0]][0] * coords[p[1]][0])
      break
      
  return circuits

def merge_circuits(circuits: list[list[int]]) -> list[list[int]]:
  circuit_set: set[int] = set([c for circuit in circuits for c in circuit]) 

  for c in circuit_set:
    elements: list[list[int]] = [circuit for circuit in circuits if c in circuit]
    for i in elements:
      circuits.remove(i)
    circuits += [list(set([e for element in elements for e in element]))]
  
  return sorted(circuits, key=lambda x: len(x), reverse=True)

part: int = 2
distances: dict[tuple[int, int], float] = calc_distances(coords)
circuits: list[list[int]] = final_circuits(1000 if part == 1 else len(distances), distances)
if part == 1: print("p1", len(circuits[0])*len(circuits[1]*len(circuits[2])))