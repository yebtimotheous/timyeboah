from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/public/<path:path>')
def serve_public(path):
    return send_from_directory('public', path)

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = 8000
    print(f"Server running at http://localhost:{port}")
    print("Press CTRL+C to stop the server")
    app.run(host='0.0.0.0', port=port, debug=True) 