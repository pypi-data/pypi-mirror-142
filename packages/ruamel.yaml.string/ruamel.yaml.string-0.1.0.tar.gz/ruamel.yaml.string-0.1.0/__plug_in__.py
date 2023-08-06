# coding: utf-8

import io

typ = 'string'

class DumpToString:
    def __init__(self, yaml):
        self.yaml = yaml

    def __call__(self, data, add_final_eol=False):
        buf = io.BytesIO()
        self.yaml.dump(data, buf)
        if add_final_eol:
            return buf.getvalue().decode('utf-8')
        else:
            return buf.getvalue()[:-1].decode('utf-8')


def init_typ(self):  # self is the YAML() instance
    self.dump_to_string = self.dumps = DumpToString(self)
