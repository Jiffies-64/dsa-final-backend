from flask import Blueprint, request
from service.UserService import UserService

UserController = Blueprint('UserController', __name__)


@UserController.route('/login', methods=['POST'])
def login():
    username = request.json.get('userName')
    password = request.json.get('password')
    remember = request.json.get('remember')
    return UserService.login(username, password)


@UserController.route('/logout', methods=['POST'])
def logout():
    return UserService.logout()
