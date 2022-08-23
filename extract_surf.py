import numpy as np
import parse_vtk as vtk

def list_faces(t):
  t = t.copy()
  np.sort(t,axis=1)
  numTets, _= t.shape 
  f = np.empty((4*numTets, 4) , dtype=int)
  for i in range(numTets):
    a = t[i, 0]
    b = t[i, 1]
    c = t[i, 2]
    d = t[i, 3]
    f[i          , :] = np.array([i,a,b,c])
    f[i+numTets  , :] = np.array([i,a,b,d])
    f[i+2*numTets, :] = np.array([i,a,c,d])
    f[i+3*numTets, :] = np.array([i,b,c,d])
  return f

def extract_unique_triangles(f):
  _, indxs, count  = np.unique(f[:,1:4], axis=0, return_index=True, return_counts=True)
  return f[indxs[count==1]]

def reconstruct(faces):
  for face in faces:
    tet = tets[face[0]]
    hasVert = [False]*4
    for j in range(4):
      for i in range(1,4):
        if face[i] == tet[j]:
          hasVert[j] = True
    face = face[hasVert]
    # f0 = [face[0],face[2],face[1]]
    # f1 = [face[0],face[3],face[2]]
    # f2 = [face[0],face[1],face[3]]
    # f3 = [face[1],face[2],face[3]]
  return faces[:,1:4]

def extract_surface(t):
  f=list_faces(t)
  f=extract_unique_triangles(f)
  f=reconstruct(f)
  return f

tets = vtk.tet_np.copy()
surf_np = extract_surface(tets)
np.savetxt("out.txt", surf_np, fmt="%d", delimiter="\t")