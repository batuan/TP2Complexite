import random
import sys
text = sys.argv[1]
size = int(sys.argv[2])
square = size*size
with open(text, 'r') as file:
    outText = text.split('.txt')[0] + 'out.txt'
    file1 = open(outText, 'w')
    line = file.read()
    solution = line.split()
    solution = list(map(int, solution))
    for i in range(0, square):
        for j in range(0, square):
            if random.random() > 0.09:
                a = int(solution[i*square+j])
                print(a, end=" ")
                file1.write(str(a))
            else:
                print(0, end=" ")
                file1.write('0')
            if j < square-1:
                file1.write(' ')
        print()
        if i < square-1:
            file1.write("\n")
    file1.close()
