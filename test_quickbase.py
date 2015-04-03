# py-quickbase - Python bindings for Intuit's QuickBase
# Copyright (C) 2012-2014 WesTower Communications
# Copyright (C) 2014-2015 MasTec
#
# This file is part of py-quickbase.
#
# py-quickbase is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

import os
import unittest

import quickbase



class TestConnect(unittest.TestCase):
    def test_connect(self):
        conn = quickbase.connect(url=os.getenv('QUICKBASE_URL'),
                                 username=os.getenv('QUICKBASE_USERNAME'),
                                 password=os.getenv('QUICKBASE_PASSWORD'))
        self.assertNotEqual(conn, None)
