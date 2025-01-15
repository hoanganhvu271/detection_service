from flask import Blueprint, jsonify, current_app, request
from app.services.detect.detect import detect

detect_bp = Blueprint('detect', __name__)


@detect_bp.route('/detect', methods=['GET'])
def detect_get():
    return jsonify({'message': 'Detect route works!'})

@detect_bp.route('/detect', methods=['POST'])
def detect_post():
    data = request.get_json()
    # print(data)
    
    # print("Method:", request.method)
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
        
    try:
        result = detect(data)
        # print(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
     
    return jsonify({'result': result})
    # return jsonify({'message': 'Detect route works!'})