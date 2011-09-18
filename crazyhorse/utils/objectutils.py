def map_form_dict(target, data):
    table = target.__dict__
    
    for key in data:
            if key in table:
                # using urlparse.parse_qs() will return results like this:
                # {'id': ['12', '32'], 'lucy': ['dog']}
                # note that the values are all lists, so if the len() of a
                # value is 1, just return the first item otherwise return
                # the whole list
                candidate = data[key]
                value     = candidate[0] if len(candidate) is 1 else candidate
                
                setattr(target, key, value)