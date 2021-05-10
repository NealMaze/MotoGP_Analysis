# imports
from importerHelpers import *

baseDir = ("C:/Users/LuciusFish/Desktop/moto_csv/")
types = ["RAC", "RAC2", "Q2", "Q1", "WUP", "FP1", "FP2", "FP3", "FP4", "Test"]

finFiles = []
with open("C:/Users/LuciusFish/Desktop/csv/finFiles.txt", "r") as f:
    contents = f.readlines()
    for i in contents:
        finFiles.append(i)

for i in finFiles:
    if i == 0 or i == []:
        del i

for sesType in Types:
    dir = baseDir + sesType
    with open(dir) as f: