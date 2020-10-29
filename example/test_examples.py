#  coding: utf-8
#  Carbon Black EDR Copyright © 2013-2020 VMware, Inc. All Rights Reserved.
################################################################################

import unittest


class TestCbFeedExamples(unittest.TestCase):
    def test_mdl(self):
        import example.mdl as mdl
        mdl.create()

    def test_tor(self):
        import example.tor as tor
        tor.create()

    def test_abusech(self):
        import example.abuse_ch as ach
        ach.create()


if __name__ == '__main__':
    # run the unit tests
    #
    unittest.main()
