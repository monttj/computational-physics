import ROOT 
import numpy as np

d = ROOT.RDataFrame("tree", "output2.root");

nd = d.Filter("dimuon_mass > 50 && dimuon_mass < 150").AsNumpy(["dimuon_mass"]); 

cols = nd["dimuon_mass"] 
print(cols)

np.save("dimuon_mass.npy", cols)
np.savetxt("dimuon_mass.txt", cols, fmt='%5.3f')
