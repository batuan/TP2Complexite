import sys

square = 0
line = []
size = int(sys.argv[2])
square = size*size
count = 0
def p(x, y, z):
    return (((x - 1) * square) + (y - 1)) * square + z

with open(sys.argv[1], 'r') as file:
    line = file.read()
    if "SAT" in line:
        print("S O L U T I O N\n- - - - - - - - -")
    solution = line.split()
    solution[0] = '0'
    solution  = list(map(int, solution))
    for i in range(1, square+1):
        for j in range(1, square+1):
            for k in range(1, square+1):
                pos = p(i, j, k)
                #print(pos)
                if(solution[pos]>0):
                    if(k<10):
                        count+=1
                        print(k, end="  ")
                    else:
                        count+=1
                        print(k, end=" ")
                    
        print()
