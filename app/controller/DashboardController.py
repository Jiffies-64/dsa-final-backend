from flask import Blueprint, request
from service.DashboardService import DashboardService
from entity.vo.Resp import Resp

DashboardController = Blueprint('DashboardController', __name__)


@DashboardController.route('/index', methods=['POST'])
def index():
    result = DashboardService.index()
    return Resp(1, "success", result).data()


@DashboardController.route('/current', methods=['POST'])
def get_current():
    user_name = request.json.get("user_name")
    result = DashboardService.get_current_user_info(user_name)
    if result is None:
        return Resp(2, "用户未登录", None).data()
    else:
        return Resp(1, "success", result).data()


@DashboardController.route('/task', methods=['POST'])
def task():
    user_name = request.json.get("user_name")
    return Resp(1, "success", []).data()
