from flask import Blueprint, request, jsonify
from service.StudentService import StudentService

StudentController = Blueprint('StudentController', __name__)


@StudentController.route('/register', methods=['POST'])
def stu_register():
    user_name = request.json.get("userName")
    password = request.json.get("password")
    user_level = request.json.get("userLevel")
    return StudentService.create_stu(user_name, password, user_level)


@StudentController.route('/current', methods=['POST'])
def get_current():
    user_name = request.json.get("user_name")
    return StudentService.get_current_user_info(user_name)


'/student/user/edit'
'/student/user/log'
'/student/user/update'
'/student/user/message/page'
'/student/user/message/read/'
'/student/user/message/unreadCount'
'/user/login'
'/user/logout'
