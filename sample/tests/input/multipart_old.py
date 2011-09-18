import urlparse
import os
import time
#import tempfile

def parse_multipart_headers(input):
    headers = input.split("\r\n")

    def split(item):
        return item.split(":")

    return { k.strip().lower():v.strip() for k,v in map(split, headers) }

def parse_mime_multipart(boundary, body):
    prefix     = "--"
    params     = {"files":{},
                  "data":{}}

    body = body.lstrip()

    f_boundary = "--" + boundary + "\r\n"

    if(body.startswith(f_boundary)):
        body = body[len(f_boundary):]

    parts = body.split(f_boundary)

    for part in parts:
        # check from the left first.
        # If we check from the right first we could hit an empty
        # value, and that throw things out of wack
        header_end  = part.find("\r\n\r\n")
        headers     = parse_multipart_headers(part[:header_end])
        disposition = headers.get("content-disposition", "")

        if not disposition: continue # malformed disposition -- no op

        first_semi_colon = disposition.find(";")

        if disposition[:first_semi_colon] != "form-data": continue #malformed disposition -- no op

        disposition = disposition[(first_semi_colon + 1):].replace('"', '')

        def split(item):
            item = item.strip()
            return item.split("=")

        meta = { k:v for k,v in map(split, disposition.split(";")) }

        if not "name" in meta: continue #malformed disposition -- no op

        if "filename" not in meta:
            value = part[header_end + 4:] # 4 = \r\n\r\n
            data  = params["data"]
            key   = meta["name"]
            if key not in data:
                data[key] = []
            data[key].append(value.strip())
        else:
            files = params["files"]
            key   = meta["name"]
            if key not in files:
                files[key] = []

            #temp = tempfile.NamedTemporaryFile(delete=False)
            #print temp.name
            #files[key].append({"filename":meta["filename"], "tmp_file":temp.name})


    return params

class FormParser(object):

    def __init__(self):
        self.files = None

    def parse_body(self, content_type, length, data):
        if length > 0:

            if content_type.startswith("application/x-www-form-urlencoded"):
                return self._parse_urlencoded(length, data)

            elif content_type.startswith("multipart/form-data"):
                # boundary= is at the end of the content_type, so
                # start looking for the 1st = from the end of the string
                index      = content_type.rfind("=") + 1
                boundary   = content_type[index:]
                params     = self._parse_multipart(length, data, boundary)
                self.files = params["files"]
                return params["data"]

        return {}

    def _parse_urlencoded(self, length, data):
        body = data.read(length)
        return urlparse.parse_qs(body)

    def _parse_multipart(self, length, data, boundary):
        body   = data.read(length)
        return parse_mime_multipart(boundary, body)

def main():
    filename = os.getcwd() + "/data-multipart-form-data-chrome.txt"
    filesize = os.path.getsize(filename)
    with open(filename) as f:
        start = time.clock()
        content_type = "multipart/form-data; boundary=----WebKitFormBoundaryy68h9UzzE0zpkUU7"
        index      = content_type.rfind("=") + 1
        boundary   = content_type[index:]
        body       = f.read(filesize)
        print(parse_mime_multipart(boundary, body))
        print(time.clock() - start)

if __name__ == "__main__":
    main()