from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from models.models import LawLLM
import torch
import threading

app = Flask(__name__, template_folder="../templates")
app.config['SECRET_KEY'] = 'secret_key'

socketio = SocketIO(app, cors_allowed_origins="*")  # 允许所有域名连接

name_space = '/llm'

llm = LawLLM()
# messages = []


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message', namespace=name_space)
def test_message(data):
    print('Received message:', data)
    emit('response', {'message': 'once'})

#
# @socketio.on('my broadcast event', namespace=name_space)
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)
#
#
# @socketio.on('connect', namespace=name_space)
# def test_connect():
#     print('Client connected')
#
#
# @socketio.on('disconnect', namespace=name_space)
# def test_disconnect():
#     print('Client disconnected')


@socketio.on('prompt', namespace=name_space)
def handle_message(prompt):
    print('Received message:', prompt)
    messages = prompt['message']
    emit('response', {'message': "<Start>"})

    def chat():
        model, tokenizer = llm.get_model_and_tokenizer()
        position = 0
        try:
            for response in model.chat(tokenizer, messages, stream=True):
                # send(response[position:])
                print(response[position:], end="", flush=True)
                emit('response', {'message': response[position:]})
                position = len(response)
                if torch.backends.mps.is_available():
                    torch.mps.empty_cache()
            emit('response', {'message': "<End>"})
        except KeyboardInterrupt:
            emit('response', {'message': "<Irpt>"})

    thread = threading.Thread(target=chat)
    thread.start()


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=5000, debug=False)
    # socketio.run(app, host="127.0.0.1", port=5000, debug=True, allow_unsafe_werkzeug=True)


# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit, send
#
# app = Flask(__name__, template_folder="../templates")
# socketio = SocketIO(app, cors_allowed_origins="*")
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @socketio.on('message')
# def handle_message(data):
#     print('Received message:', data)
#     emit('response', {'message': data['message']})
#
#
# if __name__ == '__main__':
#     socketio.run(app, host="127.0.0.1", port=5000, debug=True)
