import os
import json



def main(request):
    request_json = request.get_json(silent=True)
    for log in request_json['logs']:
        print(json.dumps(log))
    return 'done'