class TestContext(object):

    @classmethod
    def default_response(cls):
        return lambda x,y: x

    @classmethod
    def default_context(cls):
        return { 'wsgi.multiprocess': False,
                 'HTTP_REFERER': 'http://nginx:8080/index.html',
                 'REQUEST_METHOD': 'GET',
                 'PATH_INFO': '/',
                 'HTTP_ORIGIN': 'http://nginx:8080',
                 'SERVER_PROTOCOL': 'HTTP/1.1',
                 'QUERY_STRING': '',
                 'CONTENT_LENGTH': '90029',
                 'HTTP_ACCEPT_CHARSET': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1',
                 'HTTP_CONNECTION': 'keep-alive',
                 'SERVER_NAME': 'crazyhorse',
                 'REMOTE_ADDR': '127.0.0.1',
                 'wsgi.url_scheme': 'http',
                 'SERVER_PORT': '80',
                 'x-wsgiorg.uwsgi.version': '0.9.6.2',
                 'DOCUMENT_ROOT': '/usr/local/Cellar/nginx/1.0.2/html',
                 'HTTP_CONTENT_LENGTH': '90029',
                 'wsgi.input': None,#<open file 'wsgi_input', mode 'r' at 0x101103420>,
                 'HTTP_HOST': 'rodeo',
                 'wsgi.multithread': False,
                 'HTTP_CACHE_CONTROL': 'max-age=0',
                 #'HTTP_CONTENT_TYPE': 'multipart/form-data; boundary=----WebKitFormBoundaryy68h9UzzE0zpkUU7',
                 #'HTTP_CONTENT_TYPE': 'multipart/form-data; boundary=----WebKitFormBoundaryy68h9UzzE0zpkUU7',
                 'REQUEST_URI': '/',
                 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'HTTP_X_CRAZYHORSE_TEST': 'v0.1',
                 'wsgi.version': (1, 0),
                 'wsgi.run_once': False,
                 'wsgi.errors': None,#<open file 'wsgi_input', mode 'w' at 0x1012b6f60>,
                 'REMOTE_PORT': '51002',
                 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.8',
                 #'CONTENT_TYPE': 'multipart/form-data; boundary=----WebKitFormBoundaryy68h9UzzE0zpkUU7',
                 'wsgi.file_wrapper': None,#<built-in function uwsgi_sendfile>,
                 'HTTP_ACCEPT_ENCODING': 'gzip,deflate,sdch'
                }

    def __init__(self):
        pass


