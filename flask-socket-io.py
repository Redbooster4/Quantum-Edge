from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit


app = Flask(__name__)
@app.route('/')
def index():
    return "Line Saved"
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('drawing')
def handle_drawing(json_data):
    # ds a message back to the clients.
    # 'broadcast=True' sends it to everyone in the current namespace.
    # 'include_self=False' is crucial; it prevents the sender from
    # receiving their own message, which would cause redundant redraws.
    emit('drawing', json_data, broadcast=True, include_self=False)
    print(json_data)

if __name__ == '__main__':
    # The server is run using socketio.run() instead of app.run()
    # to enable WebSocket functionality.
    socketio.run(app, debug=True, port=2555)