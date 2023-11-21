from dao.Database import db
from entity.po.Subject import Subject


class SubjectService:

    @staticmethod
    def list_subject():
        return Subject.query.all()

    @staticmethod
    def select(id_):
        return Subject.query.filter_by(id=id_).first()

    @staticmethod
    def get_name_by_id(id_):
        return SubjectService.select(id_).name
