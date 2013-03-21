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
