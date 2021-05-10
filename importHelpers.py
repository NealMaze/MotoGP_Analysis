# imports
import csv
import re
from genGetters import *

def testReader(csvReader):
    prtFlg = True
    for r in csvReader:
        prtLis = []
        prtlis.append(prtlis.append(tstYr(r[0]))
        prtlis.append(tstDate(r[1]))
        prtlis.append(tstRnd(r[2]))
        prtlis.append(tstLge(r[3]))
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

def tstYr(yr):
    yrFormat = re.compile("^(199\d|20[0-5]\d)$")
    if re.match(yrFormat, yr) tst = True
    else tst = False

    return tst

def tstDate(date):
    dateFormat = re.compile("^(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[" "][0-3]\d$")
    if re.match(dateFormat, date) tst = True
    else tst = False

    return tst

def tstRnd(rnd):
    dateFormat = re.compile("^[Round_]+\d{1,2}$")
    if re.match(dateFormat, rnd) tst = True
    else tst = False

    return tst

def tstLge(lge):
    lges = getLeagues()
    if lge in lges tst = True
    else tst = False

    return tst

def tstBikNum(bkNum):
    bkNumFormat = re.compile("^\d{1,2,3}$")
    if re.match(bkNumFormat, bkNum) tst = True
    else tst = False

    return tst

def tstNat(nat):
    nats = getNations()
    if nat in nats tst = True
    else tst = False

    return tst

def tstTyre(r[0]):
    

def tstSeqLp(r[0]):

def tstTme(r[0]):

def tstAvgSpd(r[0]):