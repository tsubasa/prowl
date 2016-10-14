from __future__ import print_function

import re

class ProwlError(Exception):
    """Prowl exception"""

    def __init__(self, reason):
        self.reason = re.sub(r'<.*?>', '', reason.replace('\n', ''))

    def __str__(self):
        return self.reason
