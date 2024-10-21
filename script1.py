import numpy as np

str1 = input("Nums divided by sapces: ")
str2 = input("Nums divided by sapces again: ")

nums1 = []
for s in str1.split(" "):
    nums1.append(int(s))

nums2 = []
for s in str2.split(" "):
    nums2.append(int(s))  

M = np.vstack((nums1, nums2))
for i in M:
    print(i)

P = []
for i in range(len(M) + 1):
    print(M[0][i], " + ", M[1][i], " = ", M[0][i] + M[1][i])
