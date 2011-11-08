#!/usr/bin/python
# -*- coding: utf-8 -*-
# ProDy: A Python Package for Protein Dynamics Analysis
# 
# Copyright (C) 2010-2011 Ahmet Bakan
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

"""ProDy test suite.  Usage::

  from prody import *
  prody.test()
  
or::

  import prody.tests
  prody.tests.test()


Testing will use :mod:`nose` if it is available, otherwise it will use 
:mod:`unittest`.

"""

__author__ = 'Ahmet Bakan'
__copyright__ = 'Copyright (C) 2010-2011 Ahmet Bakan'

import sys
import prody
LOGGER = prody.LOGGER

try:
    import nose
    
except ImportError:
    LOGGER.warning('Failed to import nose, using unittest for testing.')
    LOGGER.info('nose is available at http://readthedocs.org/docs/nose/')
    
    if sys.version_info[:2] > (2,6):
        def test(verbosity=2, descriptions=True, stream=sys.stderr):
            testrunner = unittest.TextTestRunner(stream, descriptions, 
                                                 verbosity)
            for module in ['test_dynamics', 'test_proteins', 'test_select', 
                           'test_ensemble']:
                testrunner.run(unittest.defaultTestLoader.
                               loadTestsFromModule(__import__(module)))
    else:
        LOGGER.warning('Unit tests are compatible with Python 2.7 and later.')

else:
    from numpy.testing import Tester
    test = Tester().test

if __name__ == '__main__':
    test()
