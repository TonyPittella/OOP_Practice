# pylint: disable=no-else-continue

import pandas as pd



# csv file name: ping_oop_csv.csv
class ReadTextDriver:
    """ text to csv driver class """

    def __init__(self, text, destination):
        self._text = text
        self._destination = destination
        self._file_contents = []
        self._return_dict = {}

    def to_csv(self):
        """ creates csv file"""
        read_file = pd.read_csv(self._text)
        pd_csv = read_file.to_csv(self._destination)
        return pd_csv

    def parse_ping_request(self, out_file="pin_oop_.txt"):
        """ Parses over csv and retrives useful rows"""
        final_res = {}
        with open(out_file, 'r') as stuff:
            tmp = []
            lines = stuff.readlines()
        for row in lines:
            if row.startswith('PING'):
                continue
            elif row.startswith('---'):
                final_row_parts = row.split()
                for index, value in enumerate(final_row_parts):
                    if value.startswith("nytimes"):
                        final_row_parts.pop(index)
                        clear_cluter = value.replace(".map.fastly.", ".")
                        final_row_parts.insert(1, clear_cluter)
                final_res[final_row_parts[1]] = tmp
                tmp = []
            else:
                tmp.append(row.split())

        self._return_dict = final_res

    @property
    def text_g(self):
        """ Text getter"""
        return self._text

    @text_g.setter
    def text_s(self, text):
        """ Text setter"""
        self._text = text

    @property
    def destination_g(self):
        """ Destination getter"""
        return self._destination

    @destination_g.setter
    def destination_s(self, destination):
        """Destination setter"""
        self._destination = destination

    @property
    def return_dict_g(self):
        """ Dictionary getter"""
        return self._return_dict

    @return_dict_g.setter
    def return_dict_s(self, return_dict):
        """ Dictionary setter"""
        return_dict = {
            "URL": [],
            "PACKAGE": [],
            "IP": [],
            "BYTES": [],
            "TTL": [],
            "TIME": []
        }
        self._return_dict = {}

    @property
    def file_contents_g(self):
        """ File contents getter"""
        return self._file_contents

    @file_contents_g.setter
    def file_contents_s(self, file_contents):
        """ File contents setter"""
        self._file_contents = []


if __name__ == "__main__":
    text = r'pin_oop_.txt'
    destination = r'ping_oop_csv.csv'
    read_text = ReadTextDriver(text, destination)
    read_text.parse_ping_request()
    # pp(read_text._return_dict)
