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

# infile = file('gzlist','r')

# inlist = [line.split('\n')[0] for line in infile.readlines()]
# homedir = os.path.abspath('.')
# print homedir
# #stop
# for line in inlist:
# 	line = line.replace('\"', '')
# 	L = line.split('/')
# 	targdir = L[1]
# 	img = L[2]
# 	os.chdir(targdir)
# 	if 'gz' in img:
# 		cmd = 'gunzip ' + img
# 		os.system(cmd)
# 		unzip = img.split('.gz')[0]
# 	else:
# 		unzip = img
# 	cmd = 'resliceLattice ' + unzip + ' -zdim 45'
# 	print cmd
# 	os.system(cmd)
# 	os.chdir(homedir)

"""
def unzip(zipfile):
    """ unzips zipfile, 
    returns unzipped filename"""
    if not os.path.isfile(zipfile):
        raise IOError('%s does not exist'%(zipfile))
    cmd = 'gunzip ' + zipfile
    print cmd
    os.system(cmd)
    return  os.path.splitext(zipfile)[0]
	


def get_files(infile):
    """parse list of files from a textfile"""
    outlist = []
    with open(infile) as fid:
        for line in fid:
            newf = line.replace('\"', '').strip('\n')
            outlist.append(newf)
    return outlist
	


def reslice_image(imgPath):
    """calls to the command line to reslice the image passed to it"""
    cmd = 'resliceLattice ' + imgPath + ' -zdim 45'
    print cmd
    os.system(cmd)
	

def main(inputstuff):
    if type(inputstuff) == str:
        filelist = get_files(inputstuff)
    else:
        filelist = inputstuff
    filelist = set(filelist) #removes duplicates
    for image in filelist:
        if '.gz' in image:
            image = unzip(image)
        reslice_image(image)
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Takes a list of files (if no list is provided 
                        looks for a list in the file gzlist) and, 
                        for each file, unzips it if needed and calls 
                        'reslice <file> -zdim 45'""")
    group = perser,add_mutually_exclusive_group()
    group.add_argument('files', nargs='*', help='the files to be processed')
    group.add_argument('-l', '--filelist',
                        help="""the file containing a list of files to be processed.""", default='gzlist')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        print args
        if args.filelist:
            main(args.filelist)
        else:
            main(args.files)




# python reslice.py file1.gz file2.gz ...
# python reslice.py
# python reslice.py -l othergzlist
