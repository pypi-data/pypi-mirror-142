# coding: utf-8

import io

typ = 'bytes'

class DumpToBytes:
    def __init__(self, yaml):
        self.yaml = yaml

    def __call__(self, data, add_final_eol=False):
        buf = io.BytesIO()
        self.yaml.dump(data, buf)
        if add_final_eol:
            return buf.getvalue()
        else:
            return buf.getvalue()[:-1]


def init_typ(self):  # self is the YAML() instance
    self.dump_to_bytes = self.dumpb = DumpToBytes(self)
