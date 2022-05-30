def add_to_request_data(request_data, key, value):
    request_data._mutable = True
    request_data[key] = value
    request_data._mutable = False
    return request_data