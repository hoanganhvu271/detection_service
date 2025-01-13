from flask import Blueprint, jsonify

detect_bp = Blueprint('detect', __name__)

@detect_bp.route('/detect', methods=['GET'])
def detect():
    return jsonify({'message': 'Detect route works!'})
