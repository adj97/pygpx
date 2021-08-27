import xml.etree.ElementTree as et
import os
import sys

from methods import getgaps, sysprint
from classes import xmldatetime

def main():
    # welcome
    sysprint("Manipulating .gpx with pygpx", 1)
    
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
        sysprint("Check your directory and try again", 1)
        sysprint("Exiting pygpx")
        sys.exit()
    else:
        sysprint("Merging %d files:" % len(filenames))

    # load xml 
    xmlroots = []
    for filename in filenames:
        sysprint(" - " + filename)
        xmlroots.append(et.parse(filename).getroot())

    # calculate time gaps
    gaps = getgaps(xmlroots)

if  __name__ == "__main__":
    main()