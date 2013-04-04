import unittest
import os
import reslice as rs
import tempfile
from numpy.testing import (assert_raises, assert_equal, assert_almost_equal)

def test_unzip():
    tmpdir = tempfile.mkdtemp()
    orig_file = os.path.join(tmpdir, 'tempfile.txt')
    with open(orig_file, 'w+') as fid:
        fid.write('nonsense')
    os.system('gzip %s'%(orig_file))
    gzipped_file = orig_file + '.gz' 
    unzipped_file = rs.unzip(gzipped_file)
    assert_equal(unzipped_file, orig_file)
    assert_raises(IOError, rs.unzip, 'imnotafile.gz')
    
    ## clean up
    os.system('rm -rf %s'%(tmpdir))

def test_get_files():
    infile = 'gzlist'
    files_to_reslice = rs.get_files(infile)
    assert_equal(files_to_reslice[0], 
                 './B05-201/B05-201_flair.nii.gz')

