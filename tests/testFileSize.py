import numpy as np
import os
import unittest
import lsst.utils.tests
from lsst.utils import getPackageDir


def setup_module(module):
    lsst.utils.tests.init()


class MapSizeUnitTest(unittest.TestCase):
    """
    Check that the files in this package are as large as we would expect
    if git-lfs worked properly
    """

    longMessage = True

    def setUp(self):
        self.lfs_msg = '\nYou may not have git-lfs installed ' + \
                       'on your system\n' + \
                       'http://developer.lsst.io/en/latest/tools/git_lfs.html'

    def testDustMaps(self):
        """
        Go through contents of DustMaps directory and check that files
        are the size we expect them to be.
        """
        mb = 1024*1024  # because os.path.getsize returns the size in bytes
        kb = 1024
        control_size_dict = {'SFD_dust_4096_ngp.fits': 64*mb,
                             'SFD_dust_4096_sgp.fits': 64*mb,
                             'dust_nside_1024.npz': 96*mb,
                             'dust_nside_128.npz': 1.5*mb,
                             'dust_nside_16.npz': 24*kb,
                             'dust_nside_2.npz': 582,
                             'dust_nside_256.npz': 6*mb,
                             'dust_nside_32.npz': 96*kb,
                             'dust_nside_4.npz': 1.7*kb,
                             'dust_nside_512.npz': 24*mb,
                             'dust_nside_64.npz': 384*kb,
                             'dust_nside_8.npz': 6.2*kb}

        root_dir = getPackageDir('sims_maps')
        for file_name in control_size_dict:
            full_name = os.path.join(root_dir, 'DustMaps', file_name)
            size = os.path.getsize(full_name)
            self.assertLess(np.abs(size-control_size_dict[file_name]),
                            0.1*control_size_dict[file_name],
                            msg=self.lfs_msg)

    def testStarMaps(self):
        """
        Test that the files in the StarMaps directory are all several
        megabytes in size
        """

        root_dir = os.path.join(getPackageDir('sims_maps'), 'StarMaps')
        list_of_files = os.listdir(root_dir)
        for file_name in list_of_files:
            full_name = os.path.join(root_dir, file_name)
            self.assertGreater(os.path.getsize(full_name), 1024*1024,
                               msg=self.lfs_msg)


class MemoryTestClass(lsst.utils.tests.MemoryTestCase):
    pass

if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
