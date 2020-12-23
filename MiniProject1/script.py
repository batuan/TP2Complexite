import subprocess

command = ['./mini1', '../TestData/datagraph/graph25.txt', '5']

for i in range(1, 21):
    command[1] = '../TestData/mini1/cnf/graph' + str(i) + '_2CNF.txt'
    command[2] = '../TestData/mini1/affect/graph' + str(i) +'.txt'
    subprocess.run(command)
