from flask import Blueprint, jsonify, request

word_api = Blueprint('word_api', __name__)

@word_api.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Salom, dunyo!"})

@word_api.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"echo": data})