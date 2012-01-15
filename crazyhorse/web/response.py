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
        # points to the same object as 
        # request.cookies
        self.cookies = None
        self.headers = Headers()
        self.status  = ResponseStatus.OK
        self.out     = []
        self.result  = None

    def write(self, value):
        self.out.append(value)

    def __iter__(self):
        return iter(self.out)

    def __call__(self, context):
        result = self.result
        
        # TODO 
        # cached response could you the wsgi.sendfile option?

        value = None

        try:
            self.headers.add("Content-Type", result.content_type)
        except Exception as e:
            crazyhorse.get_logger().error(e.message)

        if result is not None:
            try:
                value = result()
            except Exception as e:
                crazyhorse.get_logger().error(str(e))

        if value is not None:
            self.out.append(value.encode("utf-8"))

        # set the response cookies to override
        # existing cookies or set new cookies
        # the cookies feature may not be enabled
        try:
            for cookie in self.cookies.header_items():
                self.headers.add("Set-Cookie", cookie)
        except AttributeError:
            pass

        context.start_response(self.status, self.headers.items())
        #except Exception as e:
        #    print(e.message)
        return self
