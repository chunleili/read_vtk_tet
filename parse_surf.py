fileName = "./surf.txt" 
surf = []

def read_vtk(fileName, surf):
    with open(fileName,"r") as f:
        for line in f.readlines():
            line = line.split()
            surf.append([line[0], line[1], line[2]])


read_vtk(fileName,surf)

# copy data to numpy
import numpy as np
surf_np = np.array(surf, dtype=float).reshape((-1,3))