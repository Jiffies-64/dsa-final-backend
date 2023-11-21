import json

from entity.vo.ExamPaperVo import QuestionEditRequestVo, QuestionEditItemVo
from entity.po.Question import Question
from service.TextContentService import TextContentService, QuestionObject, QuestionItemObject


class QuestionService:

    @staticmethod
    def get_question_vo_by_id(id_):
        # question
        question_po = Question.query.filter_by(id=id_).first()
        if not question_po:
            return None

        # text_content_json
        # text_content = TextContentService.select_by_id(question.info_text_content_id).content
        # text_content_json = json.loads(text_content)
        question_object = TextContentService.get_content_class_by_id(question_po.info_text_content_id, QuestionObject)

        # return
        question_vo = QuestionEditRequestVo()
        # question_vo.init(question_po, question_object)
        # from question
        question_vo.id = question_po.id
        question_vo.question_type = question_po.question_type
        question_vo.subject_id = question_po.subject_id
        question_vo.grade_level = question_po.grade_level
        question_vo.score = str(question_po.score)  # 转换为字符串，根据实际需要进行调整
        question_vo.difficult = question_po.difficult
        # from question_object
        question_vo.title = question_object.titleContent
        question_vo.analyze = question_object.analyze
        if question_vo.question_type in (1, 3):
            # 单选、判断
            question_vo.correct = question_object.correct
        elif question_vo.question_type == 2:
            # 多选
            question_vo.correct_array = question_object.correct
        elif question_vo.question_type == 4:
            # 填空
            question_vo.correct_array = question_object.correct
        else:
            # 问答
            question_vo.correct = question_object.correct
        # from items
        question_vo.items = question_object.questionItemObjects
        return question_vo

    @staticmethod
    def get_question_vo_lst_by_ids(ids, order_index):
        question_vo_lst = []
        for each_id in ids:
            question_vo = QuestionService.get_question_vo_by_id(each_id)
            if question_vo:
                question_vo.item_order = order_index
                order_index += 1
                question_vo_lst.append(question_vo)
        return question_vo_lst
