import urlparse
import crazyhorse
from crazyhorse.features.params import ParamCollection
from crazyhorse.features.requests import multipart

def feature_forms(context):
    content_length = -1
    content_type   = context.environ.get("CONTENT_TYPE", "application/unknown")
    data           = context.environ.get("wsgi.input", None)
    params         = {}
    files          = {}

    try:
        content_length = int(context.environ.get("CONTENT_LENGTH", "0"))
    except ValueError:
        pass

    if content_length > 0:
            
            if content_type == "application/x-www-form-urlencoded":
                params = urlparse.parse_qs(data.read(content_length))

            elif content_type.startswith("multipart/form-data"):
                index    = content_type.rfind("=") + 1
                boundary = content_type[index:]
                
                parser = None

                try:
                    parser   = multipart.MultipartParser(boundary, data)
                    params   = parser.params
                    files    = parser.files
                except multipart.MultipartException:
                    crazyhorse.get_logger().error("Failed to parse multipart/form-data")
                    pass

    context.request.data  = ParamCollection(params)
    context.request.files = ParamCollection(files)

