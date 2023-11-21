from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import eventlet

eventlet.monkey_patch()

app = Flask("chatWare", static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = "bruh"
socketio = SocketIO(app)


@app.route("/")
def main():
    return render_template("index.html")


# 2
@socketio.on('message')
def handleMessage(msg):
    print("收到: " + msg)
    send(msg, broadcast=True)


# 4
@socketio.event
def sendMsg(message):
    print(message)
    emit('SendtoAll', {"msg": message["msg"], "user": request.sid}, to=message["room"])


@socketio.event
def joinRoom(message):
    global Room
    print(message)
    join_room(message['room'])

    emit("roomJoined", {
        "user": request.sid,
        "room": message['room']
    }, to=message['room'])


@socketio.event
def leaveRoom(message):
    print(message)
    emit('roomLeftPersonal', {"room": message['room'], "user": request.sid})
    leave_room(message['room'])
    emit('roomLeft', {"room": message['room'], "user": request.sid}, to=message['room'])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
    socketio.run(app)
