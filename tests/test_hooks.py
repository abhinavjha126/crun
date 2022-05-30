#!/bin/env python3
# crun - OCI runtime written in C
#
# Copyright (C) 2017, 2018, 2019 Giuseppe Scrivano <giuseppe@scrivano.org>
# crun is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# crun is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with crun.  If not, see <http://www.gnu.org/licenses/>.

from tests_utils import *

def test_fail_prestart():
    conf = base_config()
    conf['hooks'] = {"prestart" : [{"path" : "/bin/false"}]}
    add_all_namespaces(conf)
    try:
        out, _ = run_and_get_output(conf)
    except:
        return 0
    return -1

def test_success_prestart():
    conf = base_config()
    conf['hooks'] = {"prestart" : [{"path" : "/bin/true"}]}
    add_all_namespaces(conf)
    try:
        out, _ = run_and_get_output(conf)
    except:
        return -1
    return 0

all_tests = {
    "test-fail-prestart" : test_fail_prestart,
    "test-success-prestart" : test_success_prestart,
}

if __name__ == "__main__":
    tests_main(all_tests)
