import subprocess

command = ['./mini2', '../TestData/datagraph/graph25.txt', '5']

for i in range(20, 26):
    #command[1] = '../TestData/datagraph/graph' + str(i) +'.txt'
    command[2] = str(i)
    subprocess.run(command)
