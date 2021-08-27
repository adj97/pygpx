import xml.etree.ElementTree as et
import os
import sys

from methods import getgaps, sysprint, getnewroots, registerxmlnamespaces
from classes import xmldatetime

def main():
    registerxmlnamespaces()

    # welcome
    sysprint("Manipulating .gpx with pygpx")

    # new filename
    newfilename = "merged" + ".gpx"

    # clean up old files
    if os.path.exists(newfilename):
        os.remove(newfilename)
    
    # get all gpx file names in current directory
    filenames = []
    for file in os.listdir():
        if file.endswith(".gpx"):
            filenames.append(file)
        else:
            continue
    
    # sort into order (probably already done by os by default)
    filenames.sort()

    # no files found error
    if(filenames == []):
        sysprint("No gpx files found")
        sysprint("Check your directory and try again")
        sysprint("Exiting pygpx")
        sys.exit()
    else:
        sysprint("Merging %d files:" % len(filenames))

    # load xml 
    xmltrees = []
    xmlroots = []
    for filename in filenames:
        sysprint(" - " + filename)
        
        xmltrees.append(et.parse(filename))
        xmlroots.append(xmltrees[-1].getroot())

    # calculate time gaps
    sysprint("Calculating time gaps")
    gaps = getgaps(xmlroots)

    # do the time increase and generate a set of new xml root objects
    sysprint("Modifying timestamps")
    newxmlroots = getnewroots(xmlroots, gaps)

    # merge the files
    # stitch trkpt elements into an xml file in order
    mergedtree = xmltrees[0]

    for newxmlroot in newxmlroots[1:]:
        for trkpt in newxmlroot[1][2]:
            mergedtree.getroot()[1][2].append(trkpt)

    # write new file
    sysprint("Writing to file " + newfilename + "")
    mergedtree.write(newfilename, encoding='utf-8', xml_declaration=True)

    sysprint("Finished")


if  __name__ == "__main__":
    main()