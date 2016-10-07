# -*- coding: utf-8 -*-

import re

class ProwlError(Exception):
    """Prowl exception"""

    def __init__(self, reason):
        self.reason = re.sub(r'<.*?>', '', reason.replace('\n', ''))

    def __str__(self):
        return self.reason
