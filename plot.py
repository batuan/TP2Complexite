import matplotlib.pyplot as plt
import numpy as np
vertex = [6, 10, 12, 14, 15, 18, 20, 25, 28, 30, 35, 40, 45, 50, 60, 75, 90, 100, 120, 140, 160, 180, 300, 500]

redution3 = [0.001445, 0.002007, 0.001867, 0.002724, 0.001876, 0.002648, 0.003586, 0.005432, 0.005328, 0.007188, 0.007427, 0.009517, 0.010332, 0.012868, 0.013224, 0.016475, 0.020596, 0.040419, 0.056898, 0.080393, 0.097779, 0.107054, 0.285447, 0.671332]
minisat3 = [0.004042, 0.003921, 0.004984, 0.004279, 0.004923, 0.006296, 0.007058, 0.007876, 0.007612, 0.00818, 0.010337, 0.008764, 0.014056, 0.014543, 0.014495, 0.020951, 0.041953, 0.069529, 0.119765, 0.166737, 0.304756, 0.345031, 1.70284, 4.33462]
bruteforce3 = [0.000060, 0.000181, 0.000280, 0.000387, 0.000535, 0.000512, 0.001526, 0.002950, 0.004557, 0.005858, 0.010878, 0.014551, 0.024613, 0.039154, 0.049515, 0.107723, 0.208821, 0.523309, 1.049552, 1.918508, 3.129146, 4.814180, 36.712590, 158.013677]

vertex4 = [10, 12, 14, 15, 18, 20, 25, 28, 30, 35, 40, 45, 50, 60, 75, 90, 100, 120, 140, 160, 180, 300, 500]
redution4 = [0.002407, 0.002723, 0.002877, 0.002775, 0.002785, 0.003585, 0.003974, 0.005282, 0.006229, 0.007820, 0.008785, 0.020064, 0.024649, 0.016451, 0.021447, 0.029250, 0.061738, 0.078445, 0.097212, 0.136282, 0.169127, 0.476724, 0.861569]
minisat4 =  [0.004517, 0.00568, 0.006649, 0.006655, 0.007731, 0.009424, 0.008492, 0.008196, 0.01043, 0.011999, 0.017478, 0.026894, 0.033367, 0.020511, 0.03687, 0.049036, 0.142796, 0.2203, 0.325209, 0.493987, 0.772953, 4.10066, 7.22198]
bruteforce4 = [0.001782, 0.005349, 0.005334, 0.007249, 0.022916, 0.041073, 0.060597, 0.106968, 0.152220, 0.329229, 0.601821, 1.085635, 1.965024, 5.217030, 16.330313, 38.792256, 62.736851, 146.137437]

# k=3
# plt.plot(np.array(vertex), np.array(redution3)*1000, color='r')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (ms)")
# plt.title("Time of reduction zone-vide to dimacs")
# plt.show()

# plt.plot(np.array(vertex), np.array(minisat3), label="minisat", color='r')
# plt.plot(np.array(vertex), np.array(bruteforce3), label="brute-force", color='b')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (s)")
# plt.title("Runtime comparison between minisat and brute-force")
# plt.legend()
# plt.show()

# k = 4
# plt.plot(np.array(vertex4), np.array(redution4)*1000, color='r')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (ms)")
# plt.title("Time reduction Zone-Vide to DIMAC CNF")
# plt.show()


# plt.plot(np.array(vertex4), np.array(minisat4), label="minisat", color='r')
# plt.plot(np.array(vertex[0:len(bruteforce4)]), np.array(bruteforce4), label="brute-force", color='b')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (seconds)")
# plt.title("Runtime comparison between minisat and brute-force when k = 4")
# plt.legend()
# plt.show()

#k=5
vertex5 = [12, 14, 15, 18, 20, 25, 28, 30, 35, 40, 45, 50, 60, 75, 90, 100, 120, 140, 160, 180, 300, 500]
redution5 = [0.002007, 0.002498, 0.002918, 0.003530, 0.004085, 0.006317, 0.007316, 0.010920, 0.013120, 0.013373, 0.016172, 0.023309, 0.019188, 0.030859, 0.053926, 0.096255, 0.117894, 0.149247, 0.238012, 0.248712, 0.669867, 1.123360]
minisat5 = [0.005463, 0.00658, 0.007722, 0.022365, 0.014166, 0.01042, 0.010667, 0.013243, 0.016136, 0.022039, 0.031378, 0.037211, 0.031736, 0.052914, 0.078488, 0.21068, 0.367859, 0.575456, 0.983745, 1.59633, 7.10525, 12.2842]
bruteforce5 = [0.071944, 0.075063, 0.105196, 0.430687, 0.803965, 2.817249, 5.573513, 8.708143, 10.183485, 19.517655, 41.746896, 88.835843, 441.210309]

# plt.plot(np.array(vertex5), np.array(redution5)*1000, color='r')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (ms)")
# plt.title("Time reduction Zone-Vide to DIMAC CNF")
# plt.show()


# plt.plot(np.array(vertex5), np.array(minisat5), label="minisat", color='r')
# plt.plot(np.array(vertex[0:len(bruteforce5)]), np.array(bruteforce5), label="brute-force", color='b')
# plt.xlabel("Number of vertex")
# plt.ylabel("Time (seconds)")
# plt.title("Runtime comparison between minisat and brute-force")
# plt.legend()
# plt.show()



# n = 150
# vertex = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# reduction = [0.055401, 0.073819, 0.103719, 0.161625, 0.183965, 0.222734, 0.299173, 0.324997, 0.384501, 0.450563, 0.524700, 0.586643, 0.695295, 0.755620, 0.845486, 0.938475, 1.037700, 1.206960, 1.345904]
# minisat = [0.105016, 0.182617, 0.312489, 0.440014, 0.672449, 0.927154, 1.34743, 1.61592, 2.13527, 2.5392, 3.4725, 3.97254, 4.81612, 6.06283, 6.72417, 7.71152, 9.18252, 11.124, 20.3523]

# plt.plot(np.array(vertex), np.array(minisat), label="minisat", color='r', marker='o')
# plt.plot(np.array(vertex), np.array(reduction), label="reduction", color='b', marker='x')
# plt.xlabel("Size of Zone-Vide")
# plt.ylabel("Time (seconds)")
# plt.title("Time reduction and solve zone vide with graph 150 vertex")
# plt.legend()
# plt.show()

#sudoku

# n = [3, 4, 5, 6, 7, 8, 9, 10]
# reduction = [0.003446, 0.030285, 0.163074, 0.719356, 2.583097, 6.775939, 18.516829, 39.625361]
# minisat = [0.005443, 0.073779, 0.127327, 0.604029, 1.74555, 4.04371, 12.4019, 25.7727]
# filesize = [0.1, 1.3, 8.3, 38.3, 151, 436, 1146.88, 2713.6]
# pre = [31, 97, 377, 784, 2165, 3756, 5979, 9120]
# # plt.plot(np.array(n), np.array(minisat), label="minisat", color='r', marker='o')
# # plt.plot(np.array(n), np.array(reduction), label="reduction", color='b', marker='x')
# #plt.plot(np.array(n), np.array(filesize), label="filesize", color='b', marker='x')
# plt.plot(np.array(n), np.array(filesize), label="cells", color='r', marker='x')
# plt.xlabel("Size of Sudoku")
# # plt.ylabel("Size (Mb)")
# plt.ylabel("pre-assigned (cells)")
# # plt.ylabel("Time (seconds)")
# # plt.title("Time reduction and solve Sudoku ")
# # plt.title("Size of DIMAC CNF file After Reduction")
# plt.title("Pre-assigned cell of Sudoku ")
# plt.legend()
# plt.show()

#mini1

var = [30, 50, 60, 70, 75, 90, 100, 125, 140, 150, 175, 200, 225, 250, 300, 375, 450, 500, 600, 700]
clause = [515, 1695, 2225, 2995, 3235, 4895, 6025, 9585, 11945, 13635, 18215, 23925, 30085, 37015, 33985, 52695, 74935, 151465, 216765, 296305]
time = [0.000008, 0.000006, 0.000007, 0.000007, 0.000020, 0.000008, 0.000006, 0.000007, 0.000010, 0.000007, 0.000020, 0.000008, 0.000012, 0.000009, 0.000007, 0.000011, 0.000010, 0.000015, 0.000021, 0.000030]

# plt.plot(np.array(var), np.array(time)*1000, label="variable", color='r', marker='o')
plt.plot(np.array(clause), np.array(time)*1000, label="clauses", color='r', marker='o')
plt.xlabel("Number of variable")
plt.ylabel("Time (ms)")
plt.title("Time Verify Sat problem")
plt.legend()
plt.show()


