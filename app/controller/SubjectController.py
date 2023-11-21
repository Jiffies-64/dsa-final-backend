from flask import Blueprint, request
from service.SubjectService import SubjectService
from entity.vo.Resp import Resp

SubjectController = Blueprint('SubjectController', __name__)


@SubjectController.route('/list', methods=['POST'])
def list_subject():
    result = SubjectService.list_subject()
    return Resp(1, "success", result).data()


@SubjectController.route('/select/<int:id_>', methods=['POST'])
def select(id_):
    result = SubjectService.select(id_)
    if result is None:
        return Resp(2, "none", None).data()
    else:
        return Resp(1, "success", result).data()
