import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from flask import Flask
from flask_cors import CORS
from backend.routes.monitor_routes import monitor_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(monitor_bp)

if __name__ == '__main__':
    app.run(debug=True)

