# imports
from importerHelpers import *

baseDir = ("C:/Users/LuciusFish/Desktop/moto_csv/")
types = ["RAC", "RAC2", "Q2", "Q1", "WUP", "FP1", "FP2", "FP3", "FP4", "Test"]
yrs = ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014",
       "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000",]

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
    filter_files = fnmatch.filter(listdir(dir)), f"{yr}"






