# imports
import csv

def getFinFiles():
    finFiles = []
    with open("C:/Users/LuciusFish/Desktop/csv/finFiles.txt", "r") as f:
        contents = f.readlines()
        for i in contents:
            finFiles.append(i)

    for i in finFiles:
        if i == 0 or i == []:
            del i

    return finFiles

def testReader(csvReader):
    prtFlg = True
    for r in csvReader:
        prtLis = []
        prtlis.append(prtlis.append(tstYr(r[0]))
        prtlis.append(tstDate(r[1]))
        prtlis.append(tstRound(r[2]))
        prtlis.append(tstLeague(r[3]))
        prtlis.append(tstBikNum(r[6]))
        prtlis.append(tstNat(r[10]))
        prtlis.append(tstTyre(r[14]))
        prtlis.append(tstTyre(r[15]))
        prtlis.append(tstSeqLp(r[18]))
        for i in r[19:28]:
            prtlis.append(tstTme(i))
        prtlis.append(tstAvgSpd(r[28]))
        if False in prtLis:
            prtFlg = False
            break
    return prtFlg

def tstYr(r[0]):

def tstDate(r[0]):

def tstRound(r[0]):

def tstLeague(r[0]):

def tstBikNum(r[0]):

def tstNat(r[0]):

def tstTyre(r[0]):

def tstSeqLp(r[0]):

def tstTme(r[0]):

def tstAvgSpd(r[0]):