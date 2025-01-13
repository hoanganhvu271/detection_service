from flask import Blueprint, jsonify, current_app, request
from app.services.detect.detect import detect

detect_bp = Blueprint('detect', __name__)


@detect_bp.route('/detect', methods=['GET'])
def detect_get():
    # data = request.get_json()
    # print(request.data)
    # print("Processing data:", data)
    # name = current_app.db.extended_datasets.find_one()['name']
    return jsonify({'message': 'Detect route works!'})

@detect_bp.route('/detect', methods=['POST'])
def detect_post():
    data = request.get_json()
    # data = request.data
    # print("Processing data:", data) 
    print("Method:", request.method)
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
        
    try:
        result = detect(data)
        print(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
     
    return jsonify({'result': result[0].tolist()})
    # return jsonify({'message': 'Detect route works!'})