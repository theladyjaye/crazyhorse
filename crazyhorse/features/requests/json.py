import crazyhorse
import json

def feature_json(context):
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
            try:
                params = json.loads(data.read(content_length))
            except ValueError:
                pass
    
    context.request.data  = ParamCollection(params)
    context.request.files = ParamCollection(files)