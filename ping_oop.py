
"""
ip address
url (domain name)
amount of bytes pinged
time (ms)
stats
23 packets transmitted, 23 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 18.689/28.368/45.696/7.491 ms

Possible classes:
PingRequest
-ip_address
-amount_of_bytes
...

Network:

fields:
-ping_requests = [PingRequest]

methods:
-get_requests:
-find_average:
-send requests (use python subprocess or open to call 'ping')

PingRequest:
-ip_address
-amount_of_bytes


-What is a class?
- What is a field?
- What does a class have? -> what are the fields

Create getters/setters

"""
#from pprint import pprint as pp
from ping_csv_class import ReadTextDriver


class PingRequest:
    """ class that maps what goes in to a ping request"""

    def __init__(self, ip_address, url, amt_bytes, time_ms):
        self._url = url
        self._ip_address = ip_address
        self._amt_bytes = amt_bytes
        self._time_ms = time_ms

    @property
    def url(self):
        """ URL getter"""
        return self._url

    @url.setter
    def url(self, url):
        """ URL setter"""
        if url.endswith(".com") or url.endswith(".net"):
            return url
        else:
            return ValueError("needs to be a url ending in '.com' or '.net' ")
        self._url = url

    @property
    def ip_address(self):
        """ IP getter"""
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """ IP setter"""
        self._ip_address = ip_address

    @property
    def amt_bytes(self):
        """ Bytes getter"""
        return self._amt_bytes

    @amt_bytes.setter
    def amt_bytes(self, amt_bytes):
        """ Bytes setter"""
        self._amt_bytes = amt_bytes

    @property
    def time_ms(self):
        """ Time getter"""
        return self._time_ms

    @time_ms.setter
    def time_ms(self, time_ms):
        """ Time setter"""
        self._time_ms = time_ms


class PrintDict:
    """ Class that formats a dictionary for viewing"""

    def __init__(self, dict_input={}):
        self._dict_req = dict_input

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string_holder = ""
        for key, val in self._dict_req.items():
            string_holder += f"{self._dict_req[key]} {val}"
        return string_holder


class PingGroup(PrintDict):
    """Class sets up a network simulator as information calculator"""

    def add_ping(self, ping):
        """Adds a ping to the sim"""
        if ping.url not in self._dict_req:
            self._dict_req[ping.url] = [ping]
        else:
            self._dict_req[ping.url].append(ping)

    def average_request(self, domain, num=2):
        """ Generates average request times"""
        av_comp = [entry.time_ms for entry in self._dict_req[domain]]
        return round(sum(av_comp) / len(av_comp), num)

    def min_request(self, domain, num=2):
        """ Generates minimum request times"""
        min_comp = [entry.time_ms for entry in self._dict_req[domain]]
        return round(min(min_comp), num)

    def max_request(self, domain, num=2):
        """ Generates maximum request times"""
        max_comp = [entry.time_ms for entry in self._dict_req[domain]]
        return round(max(max_comp), num)

    def info_time(self, domain, num=2):
        """ Generates avg, max, and min request times"""
        max_comp = [entry.time_ms for entry in self._dict_req[domain]]
        av_comp = [entry.time_ms for entry in self._dict_req[domain]]
        min_comp = [entry.time_ms for entry in self._dict_req[domain]]
        max_var = round(max(max_comp), num)
        min_var = round(min(min_comp), num)
        av_var = round(sum(av_comp) / len(av_comp), num)
        return f"""
                    For {domain}:
                    The average time for a request is: {av_var}ms
                    The minimum request time is: {min_var}ms
                    And the maximum time request is: {max_var}ms
                    
                """

    @property
    def dict_req_g(self):
        """ dict getter"""
        return self._dict_req

    @dict_req_g.setter
    def dict_req_s(self, dict_req):
        """ dict setter"""
        self._dict_req = dict_req


if __name__ == "__main__":
    text = r'pin_oop_.txt'
    destination = r'ping_oop_csv.csv'
    read_text = ReadTextDriver(text, destination)
    read_text.parse_ping_request()
    data = read_text.return_dict_g
    pg = PingGroup()
    for key, vals in data.items():
        vals = vals[2:-1]
        for val in vals:
            #ip_address, URL, amt_bytes, time
            if len(val) > 0:
                if "=" in val[-2]:
                    _, ms = val[-2].split("=")
                    pr = PingRequest(val[3], key, val[0], float(ms))
                    pg.add_ping(pr)

    print(pg.info_time("facebook.com"))
    print(pg.info_time('reddit.com'))
    print(pg.info_time('nytimes.net'))
    print(pg.info_time('google.com'))
