
# module to hold all utilities/helper functions

import json

from flask import make_response, current_app


# return a list of dicts as json with correct mime types
# flask does not provide a jsonify for lists; hence this method
def jsonify_list(data):
    if type(data) is not list:
        raise Exception('jsonify_list function accepts only a list')

    return make_response(json.dumps(data), 200,
                         {'content-type': 'application/json'})

# take in a flask request object and try to parse out a dictionary from the
# request
# try to find if request is as JSON first, then look into forms, finally force
# find it.
# If not found return a dict; else return the parsed data
