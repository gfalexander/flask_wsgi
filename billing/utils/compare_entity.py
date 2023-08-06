from copy import deepcopy

from .exceptions import InvalidTypeException, MissingKeyException


def validate_body(request_dict, dto):
    
    if not isinstance(request_dict, dict):
        raise Exception("Body must be a dict")

    dto_dict = deepcopy(dto.__dict__())

    error_missing_key = []
    error_invalid_type = []

    

    for key in dto_dict:
        if key not in request_dict:
            error_missing_key.append(key)
            continue

        if not isinstance(request_dict[key], type(dto_dict[key])):
            error_invalid_type.append(key)

    if error_missing_key:
        message = "Missing key(s): " + ", ".join(error_missing_key)
        raise MissingKeyException(message)

    if error_invalid_type:
        message = "Invalid type(s): " + ", ".join(error_invalid_type)
        raise InvalidTypeException(message)
                
    print("OK")