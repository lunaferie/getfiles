#!/usr/bin/python
# v3.1
# history of changes:
#	v3.1 - add single link from cli: -l parametr
#	v3.0 - remove automatic extension and add parametrs from command line
# 	v2.3 - add extensions to downloaded files and comments in script
#
################################################
 
import urllib
import os
import sys
import getopt

files = []

try:
    shortargs = "n:a:l:"
    longargs = ['help']
    options, args = getopt.gnu_getopt(sys.argv[1:], shortargs, longargs)
except getopt.GetoptError as err:
    print str(err)
    print 'use --help'
    sys.exit(2)

for chose, value in options:
    if chose == '-n':
        outfile = value

    if chose == '-a':
        with open(value, 'r') as links:
	    files = links.readlines()

    if chose == '-l':
	x = value
	files.append(value)

    if chose == '--help':
        print "-n	enter name for downloaded files"
	print "-a	add links from file"
	print "-l	add single link from cli"
	files.append('1')

if not files:
    print 'no arguments'
    print 'use --help'
    sys.exit(3)

elif files == ['1']:
    sys.exit(4)

print "-------------------------\n"

# Percent progres function (blockSize and totalSize are the data get from url)
def progres(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()

# Function to get files, when file is downloaded, she call progress function='reporthook=progres'  
def getf(getFile, saveFile):
    sys.stdout.write('\rFetching ' + getFile + '...\n')
    urllib.urlretrieve(getFile, saveFile, reporthook=progres)
    sys.stdout.write("\rDownload complete, saved as: " + '\n\n')
    sys.stdout.flush()

# check length of files list and increment +1 (because counter=1)
counter=1
counter=int(counter)
lenght = len(files) + 1

# existing file name
fileexist="%s.part%d" % (outfile, counter)

# call getf function, to download files from files LIST
for getFile in files:
    getf(getFile, outfile)

# while file name exist in our path, increment name +1 (our+file.part+1)
    while os.path.exists(fileexist) == True:
	counter+=1
	lenght+=1
	fileexist="%s.part%d" % (outfile, counter)

# if link to download in file LIST > 1 (counter=1) then: 
# change name and add extension to file, get downloaded file size in KB, MB or GB and print that

    if lenght > counter:
        os.system('mv %s %s.part%d' % (outfile, outfile, counter))
        file = '%s.part%d' % (outfile, counter)
	print file
	filesize = os.path.getsize(file)
	total = (filesize/1024)/1024
	
	if total <= 0:
	    total = (filesize/1024)
	    print "Size: %d KB" % total
	
	elif total > 1024:
	    total = float((filesize/1024)/1024)/1024
	    print "Size: %d GB" % total
	
	else:
	    print "Size: %d MB" % total	
	
	print "-------------------------\n"

