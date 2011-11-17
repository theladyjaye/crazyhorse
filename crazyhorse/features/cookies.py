# http://www.quirksmode.org/js/cookies.html
# http://en.wikipedia.org/wiki/HTTP_cookie
# Cookie: name=value; name2=value2
# environ["HTTP_COOKIE"] = name=value; name2=value2

import urllib
import datetime
import email.utils
import calendar

def feature_cookies(context):
    feature = CookieHandler(context.environ.get("HTTP_COOKIE", None))
    
    context.request.cookies  = feature
    context.response.cookies = CookieHandler()


class CookieHandler(object):
    """
    http://www.quirksmode.org/js/cookies.html
    First the name-value pair ('ppkcookie1=testcookie')
    then a semicolon and a space
    then the expiry date in the correct format ('expires=Thu, 2 Aug 2001 20:47:11 UTC')
    again a semicolon and a space
    then the path (path=/)
    'ppkcookie2=another test; expires=Fri, 3 Aug 2001 20:47:11 UTC; path=/'
    """
    def __init__(self, data=None):
        self.cookies = {}

        if data is not None:
            self.parse(data)


    def add(self, name, value, path="/", expires=None, domain=None, secure=None, httponly=None):

        if expires is not None:

            if type(expires) is not datetime.datetime:
                raise TypeError("Cookie expire time must be a datetime")
            else:
                #Wdy, DD-Mon-YYYY HH:MM:SS GMT
                time_tuple = calendar.timegm(expires.utctimetuple())
                expires    = email.utils.formatdate(time_tuple, localtime=False, usegmt=True)

        self.cookies[name] = {"value":urllib.quote_plus(value),
                                "path":path,
                                "expires":expires if expires is not None else None,
                                "domain":domain,
                                "secure":secure,
                                "httponly":httponly
                                }
    def header_items(self):
        # Set-Cookie: name=foo; Domain=.foo.com; Path=/; Expires=Wed, 13-Jan-2021 22:23:01 GMT; HttpOnly

        for key in self.cookies:
            parts = []
            parts.append(urllib.quote_plus(key) + "=" + self.cookies[key]["value"])

            if self.cookies[key]["path"] is not None:
                parts.append("path=" + self.cookies[key]["path"])

            if self.cookies[key]["expires"] is not None:
                parts.append("expires=" + self.cookies[key]["expires"])

            if self.cookies[key]["domain"] is not None:
                parts.append("domain=" + self.cookies[key]["domain"])

            if self.cookies[key]["secure"] is not None:
                parts.append("secure")

            if self.cookies[key]["httponly"] is not None:
                parts.append("HttpOnly")

            yield "; ".join(parts)


    def items(self):
        for key in self.cookies:
            yield key, self.cookies[key]

    def parse(self, data):
        data = [tuple(item.strip().split("=")) for item in data.split(";")]

        for item in data:
            self.cookies[urllib.unquote_plus(item[0])] = { "value":urllib.unquote_plus(item[1]) }


    def __len__(self):
        return len(self.cookies)

    def __getitem__(self, key):
        try:
            return self.cookies[key]["value"]
        except KeyError as e:
            return None