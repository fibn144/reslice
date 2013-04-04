import argparse
import os
import sys
"""
if len(sys.argv) < 2:
	print 'usage '
	print 'python reslice.py <list of new subjects>'
	print ''
	print 'chaque ligne doit etre en format de:'
	print '\"./B10-223/B10-223_flair.nii.gz\"'
	print ''
	sys.exit()
"""
infile = file('gzlist','r')

inlist = [line.split('\n')[0] for line in infile.readlines()]
homedir = os.path.abspath('.')
print homedir
#stop
for line in inlist:
	line = line.replace('\"', '')
	L = line.split('/')
	targdir = L[1]
	img = L[2]
	os.chdir(targdir)
	if 'gz' in img:
		cmd = 'gunzip ' + img
		os.system(cmd)
		unzip = img.split('.gz')[0]
	else:
		unzip = img
	cmd = 'resliceLattice ' + unzip + ' -zdim 45'
	print cmd
	os.system(cmd)
	os.chdir(homedir)








parser = argparse.ArgumentParser(
    description="""Takes a list of files (if no list is provided looks for a 
list in the file gzlist) and, for each file, unzips it and calls 
'reslice <file> -zdim 45'""")
parser.add_argument("files", nargs="*", help="the files to be processed")

def main(cmdargs):
    args = parser.parse_args(cmdargs)
    filelist = []
    if len(args.files) == 0:
	    filelist += getfiles(filelistFilename)
    else:
	    filelist += args.files
    filelist = set(filelist)

if __name__ == '__main__':
    main(sys.argv)


# python reslice.py file1.gz file2.gz ...
# python reslice.py
