# imports
from importHelpers import *

dir = ("C:/Users/LuciusFish/Desktop/moto_csv/")
types = ["RAC", "RAC2", "Q2", "Q1", "WUP", "FP1", "FP2", "FP3", "FP4", "Test"]
yrs = ["2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008",
       "2007", "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998"]

finFiles = getFinFiles()

for yr in yrs:
    for sesType in Types:
        filter_files = fnmatch.filter(listdir(dir)), f"{yr}*.csv"
        fileList = [f"{dir}/{file}" for file in filter_files]
        for file in filelist:
            if file not in finFiles:
                with open(file, r) as csvFile:
                    csvReader = csv.reader(csvFile, delimiter = ",")
                    importFlag = testReader(csvReader)
                    if importFlag == True:








