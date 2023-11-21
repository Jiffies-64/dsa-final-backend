import json

from entity.po.ExamPaperQuestionCustomerAnswer import ExamPaperQuestionCustomerAnswer


class QuestionAnswerService:

    @staticmethod
    def select(id_):
        pass

    @staticmethod
    def page_list(page_index, page_size):
        query = ExamPaperQuestionCustomerAnswer.query
        pagination = query.paginate(page=page_index, per_page=page_size)
        papers = pagination.items
        result = {
            "list": [paper.to_dict() for paper in papers],
            "total": pagination.total,
            "PageNum": page_index
        }
        return result
