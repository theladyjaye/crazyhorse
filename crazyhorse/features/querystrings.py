import urllib
from crazyhorse.features.params import ParamCollection

def feature_querystrings(context):

    params = None
    data   = None
    try:
        data   = urllib.parse.parse_qs(context.environ["QUERY_STRING"])
    except KeyError:
        data = {}

    params = ParamCollection(data)
    context.request.querystring = params