# -*- coding: utf-8 -*-

"""
flask_wxpay.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

import sys

# -------
# Pythons
# -------

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

if is_py2:
    from urllib.parse import urljoin

    bytes = str
    str = str  # noqa
    str = str  # noqa
    numeric_types = (int, int, float)  # noqa

elif is_py3:
    from urllib.parse import urljoin  # noqa

    str = str
    bytes = bytes
    str = (str, bytes)
    numeric_types = (int, float)
