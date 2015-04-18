#!/usr/bin/python
#
# by lunaferie
# v_4.2
################################################
 
import urllib
import os
import sys
import getopt

files = []

try:
    shortargs = "a:l:"
    longargs = ['help']
    options, args = getopt.gnu_getopt(sys.argv[1:], shortargs, longargs)
except getopt.GetoptError as err:
    print str(err)
    print 'use --help'
    sys.exit(2)

for chose, value in options:
    if chose == '-a':
        with open(value, 'r') as links:
	    files = links.readlines()

    if chose == '-l':
	x = value
	files.append(value)

    if chose == '--help':
	print "-a	add links from file"
	print "-l	add single link from cli"
	files.append('1')

if not files:
    print 'no arguments'
    print 'use --help'
    sys.exit(3)

elif files == ['1']:
    sys.exit(4)

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

# add default name
for name in files:
    st_outfile = name.split('/')[-1].strip()
    extended = name.split('.')[-1].strip()
    outfile = st_outfile.replace(extended, '')
    
# existing file name
fileexist="%spart%d.%s" % (outfile, counter, extended)

# call getf function, to download files from files LIST
for getFile in files:
    getf(getFile, outfile)

# while file name exist in our path, increment name +1 (our+file.part+1)
    while os.path.exists(fileexist) == True:
	counter+=1
	lenght+=1
	fileexist="%spart%d.%s" % (outfile, counter, extended)

# if link to download in file LIST > 1 (counter=1) then: 

    if lenght > counter:
        os.system('mv %s %spart%d.%s' % (outfile, outfile, counter, extended))
        file = '%spart%d.%s' % (outfile, counter, extended)

    print '%spart%d.%s' % ( outfile, counter, extended)
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

