import sys

square = 0
line = []
size = int(sys.argv[2])
edges = int(sys.argv[3])
vertex = []
def p(x, y):
    return (x-1)*edges + y

with open(sys.argv[1], 'r') as file:
    line = file.read()
    if "SAT" in line:
        print("Solution by minisat: \nVertex: ", end=" ")
    solution = line.split()
    solution[0] = '0'
    solution  = list(map(int, solution))
    for i in range(1, size+1):
        for j in range(1, edges+1):
            pos = p(i, j)
            if(solution[pos]>0):
                vertex.append(j)
    vertex.sort()
    for v in vertex:
        print(v, end=" ")
    print()
