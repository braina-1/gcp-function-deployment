from flask import jsonify

def hello(request):
    request_json = request.get_json(silent=True)

    abc = request_json.get('abc')

    return(abc)
