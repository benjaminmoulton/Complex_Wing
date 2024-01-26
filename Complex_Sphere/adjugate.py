import numpy as np

A = np.matrix([
    ["m","x","y","z"],
    ["-x","m","-z","y"],
    ["-y","z","m","-x"],
    ["-z","-y","x","m"]])

print(A.getH())
print(np.linalg.det(A))