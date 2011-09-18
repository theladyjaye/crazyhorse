import crazyhorse
from crazyhorse.web.headers import Headers

class ResponseStatus(object):
    OK                = "200 OK"
    MOVED_PERMANENTLY = "301 Moved Permanently"
    MOVED_TEMPORARILY = "302 Moved Temporarily"
    FORBIDDEN         = "403 Forbidden"
    NOT_FOUND         = "404 Not Found"
    SERVER_ERROR      = "500 Internal Server Error"

class Response(object):

    def __init__(self):

        self.headers = Headers()
        self.status  = ResponseStatus.OK
        self.out     = []
        self.result  = None

    def write(self, value):
        self.out.append(value)

    def __iter__(self):
        return iter(self.out)

    def __call__(self, environ, start_response):
        
        result = self.result
        
        # TODO 
        # cached response could you the wsgi.sendfile option?

        value = None

        try:
            self.headers.add("Content-Type", result.content_type)
        except Exception as e:
            crazyhorse.get_logger().error(e.message)

        if result is not None:
            value = result()

        if value is not None:
            self.out.append(value.encode("utf-8"))

        #if self.cookies is not None and session is not None:
        #    self.cookies.add(session.key, session.id, path="/")

        if self.cookies is not None and len(self.cookies) > 0:
            for cookie in self.cookies.header_items():
                self.headers.add("Set-Cookie", cookie)
            
            #self.headers.add("Set-Cookie", "PHPSESSID=ushobtc017r9eibetu6rhnjcm0", path="/")
            
        
        start_response(self.status, self.headers.items())
        #except Exception as e:
        #    print(e.message)

        return self
