# encoding: utf-8
from apps import app, socketio


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=7474)
