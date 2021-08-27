from datetime import date, datetime as dt
import datetime
import xml.etree.ElementTree as et
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
        startgpxdt = xmlroot[1][2][0][1].text
        startxdt = xmldatetime(startgpxdt)
        starts.append(startxdt)
    
    # element by element subtraction
    gaps = []
    for start, end in zip(starts, ends):
        gaps.append(start-end)

    return gaps

def getnewroots(xmlroots, gaps):

    # init
    newxmlroots = []

    # first file xmlroots[0] unchanged
    newxmlroots.append(xmlroots[0])
    
    # every later file is modified
    for i in range(1, len(gaps)+1):
        xmlroot = xmlroots[i]

        # time to trim is the total gaps up to before this file starts
        delta = dtsum(gaps[0:i])
        
        # apply time change
        newxmlroot = adjusttime(xmlroot, delta)

        newxmlroots.append(newxmlroot)

    return newxmlroots

def adjusttime(xml, dt):

    # extra time step
    buffer = datetime.timedelta(seconds=1)

    # trkpt loop
    trkseg = xml[1][2]
    for trkpt in trkseg:
        trkpt[1].text = dtToXlmdt(xmldatetime(trkpt[1].text).dt-dt+buffer).toXmlString()

    return xml

def dtsum(dtarray):
    s = dtarray[0]
    for dt in dtarray[1:]:
        s = s + dt
    return s

def dtToXlmdt(dt):
    return xmldatetime(dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")


def sysprint(string, line_bool=False):
    printgap = "  "
    print(printgap + string)
    if line_bool:
        print(printgap + "...")

def registerxmlnamespaces():
    et.register_namespace('', "http://www.topografix.com/GPX/1/1")
    et.register_namespace('ns_3', "http://www.garmin.com/xmlschemas/TrackPointExtension/v1")
    et.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
    et.register_namespace('ns_2', "http://www.garmin.com/xmlschemas/GpxExtensions/v3")
    