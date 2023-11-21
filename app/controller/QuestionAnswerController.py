from flask import Blueprint, request
from service.QuestionAnswerService import QuestionAnswerService
from entity.vo.Resp import Resp

QuestionAnswerController = Blueprint('QuestionAnswerController', __name__)


@QuestionAnswerController.route('/select/<int:id_>', methods=['POST'])
def select(id_):
    result = QuestionAnswerService.select(id_)
    if result is None:
        return Resp(2, "error", None).data()
    else:
        return Resp(1, "success", result).data()


@QuestionAnswerController.route('/page', methods=['POST'])
def page_list():
    page_index = request.json.get("pageIndex")
    page_size = request.json.get("pageSize")
    result = QuestionAnswerService.page_list(page_index, page_size)
    return Resp(1, "success", result).data()
