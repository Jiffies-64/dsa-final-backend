from flask import Blueprint, request
from service.ExamPaperService import ExamPaperService
from entity.vo.Resp import Resp

ExamPaperController = Blueprint('ExamPaperController', __name__)


@ExamPaperController.route('/select/<int:id_>', methods=['POST'])
def select(id_):
    result = ExamPaperService.select(id_)
    if result is None:
        return Resp(2, "error", None).data()
    else:
        return Resp(1, "success", result).data()


@ExamPaperController.route('/pageList', methods=['POST'])
def page_list():
    paper_type = request.json.get("paperType")
    subject_id = request.json.get("subjectId")
    page_index = request.json.get("pageIndex")
    page_size = request.json.get("pageSize")
    result = ExamPaperService.page_list(paper_type, subject_id, page_index, page_size)
    return Resp(1, "success", result).data()
