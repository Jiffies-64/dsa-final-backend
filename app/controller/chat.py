# from flask import Flask, render_template, request, copy_current_request_context
# from flask_socketio import SocketIO, send, emit
# from models.models import LawLLM
# import torch
# import time
#
# app = Flask(__name__, template_folder="../templates")
# app.config['SECRET_KEY'] = 'secret_key'
#
# socketio = SocketIO(app, cors_allowed_origins="*")  # 允许所有域名连接
#
# name_space = '/llm'
#
# llm = LawLLM()
#
#
# # messages = []
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @socketio.on('message', namespace=name_space)
# def test_message(data):
#     print('Received message:', data)
#     emit('response', {'message': 'once'})
#
#
# # @socketio.on('my broadcast event', namespace=name_space)
# # def test_message(message):
# #     emit('my response', {'data': message['data']}, broadcast=True)
#
#
# @socketio.on('connect', namespace=name_space)
# def connect():
#     print('Client connected')
#
#
# @socketio.on('ping', namespace=name_space)
# def pong(msg):
#     print('Received message:', msg)
#     while True:
#         print("Sending Pong...")
#         emit('pong', {'message': "<Pong>"})
#         socketio.sleep(0)  # 模拟上下文切换
#         time.sleep(20)
#
#
# @socketio.on('disconnect', namespace=name_space)
# def disconnect():
#     print('Client disconnected')
#
#
# # @socketio.on('prompt', namespace=name_space)
# # def handle_message(prompt):
# #     print('Received message:', prompt)
# #     messages = prompt['message']
# #     emit('response', {'message': "<Start>"})
# #
# #     @copy_current_request_context
# #     def chat():
# #         model, tokenizer = llm.get_model_and_tokenizer()
# #         position = 0
# #         try:
# #             for response in model.chat(tokenizer, messages, stream=True):
# #                 print(response[position:], end="", flush=True)
# #                 socketio.emit('response', {'message': response[position:]})
# #                 position = len(response)
# #                 if torch.backends.mps.is_available():
# #                     torch.mps.empty_cache()
# #             socketio.emit('response', {'message': "<End>"})
# #         except KeyboardInterrupt:
# #             socketio.emit('response', {'message': "<Irpt>"})
# #
# #     @copy_current_request_context
# #     def send_ping():
# #         while True:
# #             socketio.emit('response', {'message': "<Ping>"})
# #             time.sleep(5)
# #
# #     socketio.start_background_task(target=send_ping)
# #     socketio.start_background_task(target=chat)
#
#
# @socketio.on('prompt', namespace=name_space)
# def handle_message(prompt):
#     print('Received message:', prompt)
#     messages = prompt['message']
#     emit('response', {'message': "<Start>"})
#
#     @copy_current_request_context  # This decorator copies the current request context to the new thread
#     def chat():
#         model, tokenizer = llm.get_model_and_tokenizer()
#         position = 0
#         try:
#             for response in model.chat(tokenizer, messages, stream=True):
#                 print(response[position:], end="", flush=True)
#                 socketio.emit('response', {'message': response[position:]}, namespace=name_space)
#                 socketio.sleep(0)  # 模拟上下文切换
#                 position = len(response)
#                 if torch.backends.mps.is_available():
#                     torch.mps.empty_cache()
#             socketio.emit('response', {'message': "<End>"}, namespace=name_space)
#         except KeyboardInterrupt:
#             socketio.emit('response', {'message': "<Irpt>"}, namespace=name_space)
#
#     socketio.start_background_task(target=chat)
