import numpy as np
import parse_vtk as vtk

def list_faces(t):
  t.sort(axis=1)
  numTets, _= t.shape 
  f = np.empty((4*numTets, 3) , dtype=int)
  for i in range(numTets):
    a = t[i, 0]
    b = t[i, 1]
    c = t[i, 2]
    d = t[i, 3]
    f[i      , :] = np.array([a,b,c])
    f[i+numTets  , :] = np.array([a,b,d])
    f[i+2*numTets, :] = np.array([a,c,d])
    f[i+3*numTets, :] = np.array([b,c,d])
  return f

def extract_unique_triangles(t):
  _, indxs, count  = np.unique(t, axis=0, return_index=True, return_counts=True)
  return t[indxs[count==1]]

def extract_surface(t):
  f=list_faces(t)
  f=extract_unique_triangles(f)
  return f

surf_np = extract_surface(vtk.tet_np)