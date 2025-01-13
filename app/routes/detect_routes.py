from flask import Blueprint, jsonify, current_app



detect_bp = Blueprint('detect', __name__)

@detect_bp.route('/detect', methods=['GET'])
def detect():
    name = current_app.db.extended_datasets.find_one()['name']
    return jsonify({'message': 'Detect route works!' + name})

