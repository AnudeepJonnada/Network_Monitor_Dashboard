from flask import Blueprint, jsonify, request
from backend.monitor import check_all_devices, add_device

monitor_bp = Blueprint('monitor', __name__)

@monitor_bp.route('/api/status', methods=['GET'])
def status():
    return jsonify(check_all_devices())

@monitor_bp.route('/api/add-device', methods=['POST'])
def add():
    data = request.get_json()
    name = data.get('name')
    ip = data.get('ip')
    if not name or not ip:
        return jsonify({"error": "Missing name or IP"}), 400
    add_device(name, ip)
    return jsonify({"message": "Device added successfully"})

