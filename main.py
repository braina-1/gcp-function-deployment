from flask import jsonify

def hello(request):
    request_json = request.get_json(silent=True)

    return jsonify({"error":"abc"})
