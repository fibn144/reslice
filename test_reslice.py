import unittest
import os
import reslice as rs
from numpy.testing import (assert_raises, assert_equal, assert_almost_equal)

def test_unzip():
    pass

def test_get_files():
    infile = 'gzlist'
    files_to_reslice = rs.get_files(infile)
    assert_equal(files_to_reslice[0], 
                 './B05-201/B05-201_flair.nii.gz')

