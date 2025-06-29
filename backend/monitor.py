import subprocess
import json
import os
import time

DEVICES_PATH = os.path.join(os.path.dirname(__file__), '../database/devices.json')

def ping_device(ip):
    start = time.time()
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.DEVNULL)
        latency = round((time.time() - start) * 1000, 2)  # in milliseconds
        return True, latency
    except subprocess.CalledProcessError:
        return False, None

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

