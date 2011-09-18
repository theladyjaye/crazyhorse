import collections
class ParamCollection(collections.Mapping):

    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):

        value = None

        try:
            # using urlparse.parse_qs() will return results like this:
            # {'id': ['12', '32'], 'lucy': ['dog']}
            # note that the values are all lists, so if the len() of a
            # value is 1, just return the first item otherwise return
            # the whole list
            candidate = self._data[key]
            value = candidate[0] if len(candidate) is 1 else candidate
        except KeyError as e:
            pass

        return value

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)