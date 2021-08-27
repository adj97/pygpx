from classes import xmldatetime
from operator import sub

def getgaps(xmlroots):

    # get first n-1 end times as a list
    ends = []
    for xmlroot in xmlroots[:-1]:
        endgpxdt = xmlroot[1][2][-1][1].text
        endxdt = xmldatetime(endgpxdt)
        ends.append(endxdt)

    # get last n-1 start times as a list
    starts = []
    for xmlroot in xmlroots[1:]:
        startgpxdt = xmlroot[1][2][1][1].text
        startxdt = xmldatetime(startgpxdt)
        starts.append(startxdt)
    
    # element by element subtraction
    gaps = []
    for start, end in zip(starts, ends):
        gaps.append(start-end)

    return gaps

def sysprint(string, line_bool=False):
    printgap = "   "
    print(printgap + string)
    if line_bool:
        print(printgap + "...")