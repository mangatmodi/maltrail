#!/usr/bin/env python

"""
Copyright (c) 2014-2015 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content
from core.common import BLACKLIST

__type__ = (BLACKLIST.IP,)
__url__ = "http://www.openbl.org/lists/base.txt"
__check__ = "source ip"
__info__ = "abuser"
__reference__ = "openbl.org"

def fetch():
    retval = dict((_, {}) for _ in __type__)
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[BLACKLIST.IP][line] = (__info__, __reference__)

    return retval