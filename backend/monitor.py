import subprocess
import json
import os
import time
import socket

DEVICES_PATH = os.path.join(os.path.dirname(__file__), '../database/devices.json')

def ping_device(ip, port=80, timeout=2):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return "Online", 0  
    except Exception:
        return "Offline", None

def check_all_devices():
    with open(DEVICES_PATH) as f:
        devices = json.load(f)
    results = []
    for d in devices:
        status, latency = ping_device(d["ip"])
        result = {
            "name": d["name"],
            "ip": d["ip"],
            "status": status,
            "latency": latency,
            "last_seen": time.strftime('%Y-%m-%d %H:%M:%S') if status else "N/A"
        }
        results.append(result)
    return results

def add_device(name, ip):
    with open(DEVICES_PATH) as f:
        devices = json.load(f)
    devices.append({"name": name, "ip": ip})
    with open(DEVICES_PATH, 'w') as f:
        json.dump(devices, f, indent=2)
    return True

