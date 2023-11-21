from flask import Blueprint, request
from service.ExamPaperAnswerService import ExamPaperAnswerService
from entity.vo.Resp import Resp

ExamPaperAnswerController = Blueprint('ExamPaperAnswerController', __name__)


@ExamPaperAnswerController.route('/answerSubmit', methods=['POST'])
def submit():
    id_ = request.json.get("id")
    do_time = request.json.get("doTime")
    answer = request.json.get("answerItems")
    print(answer)
    result = ExamPaperAnswerService.submit(id_, do_time, answer)
    return Resp(1, "success", result).data()


@ExamPaperAnswerController.route('/pageList', methods=['POST'])
def page_list():
    page_index = request.json.get("pageIndex")
    page_size = request.json.get("pageSize")
    result = ExamPaperAnswerService.page_list(page_index, page_size)
    return Resp(1, "success", result).data()


@ExamPaperAnswerController.route('/read/<int:id_>', methods=['POST'])
def read(id_):
    result = ExamPaperAnswerService.read(id_)
    return Resp(1, "success", result).data()

