import json

from entity.po.ExamPaper import ExamPaper
from entity.vo.ExamPaperVo import ExamPaperEditRequestVo, ExamPaperTitleItemVo
from service.TextContentService import TextContentService
from service.QuestionService import QuestionService


class ExamPaperService:

    @staticmethod
    def select(id_):
        # exam_paper = ExamPaper.query.get(id)
        exam_paper = ExamPaper.query.filter_by(id=id_).first()
        if exam_paper is None:
            return None

        # Map ExamPaper to ExamPaperEditRequestVo
        vo = ExamPaperEditRequestVo()
        vo.id = exam_paper.id
        vo.level = exam_paper.grade_level
        vo.subject_id = exam_paper.subject_id
        vo.paper_type = exam_paper.paper_type
        vo.name = exam_paper.name
        vo.suggest_time = exam_paper.suggest_time
        vo.limit_date_time = [
            exam_paper.limit_start_time.strftime('%Y-%m-%d %H:%M:%S') if exam_paper.limit_start_time else None,
            exam_paper.limit_end_time.strftime('%Y-%m-%d %H:%M:%S') if exam_paper.limit_end_time else None
        ]
        vo.score = str(exam_paper.score)

        # Get frame text content and extract question IDs
        frame_text_content = TextContentService.select_by_id(exam_paper.frame_text_content_id)

        exam_paper_title_items = []
        order_index = 1
        for each_title in json.loads(str(frame_text_content.content)):
            title_vo = ExamPaperTitleItemVo()
            title_vo.name = each_title['name']
            lst = QuestionService.get_question_vo_lst_by_ids(each_title['ids'], order_index)
            title_vo.question_items = lst
            order_index += len(lst)
            exam_paper_title_items.append(title_vo)
        # vo.set_title_items(exam_paper_title_items)
        vo.title_items = exam_paper_title_items

        # # Map ExamPaperTitleItemObjects to ExamPaperTitleItemVMs
        # exam_paper_title_item_vms = [
        #     model_mapper.map(t, ExamPaperTitleItemVM, item_types=(ExamPaperTitleItemVM, QuestionEditRequestVM))
        #     for t in exam_paper_title_item_objects
        # ]
        #
        # # Set item orders for questions and add them to ExamPaperTitleItemVMs
        # for t_vm, t_obj in zip(exam_paper_title_item_vms, exam_paper_title_item_objects):
        #     t_vm.question_items = [
        #         question_service.get_question_edit_request_vm(question).update(item_order=i.item_order)
        #         for i in t_obj.question_items
        #         for question in questions
        #         if question.id == i.id
        #     ]
        #
        # vm.title_items = exam_paper_title_item_vms
        # vm.score = exam_util.score_to_vm(exam_paper.score)
        #
        # # Set limit date time if the paper type is time-limited
        # if exam_paper.paper_type == ExamPaperTypeEnum.TimeLimit.value:
        #     limit_date_time = [datetime_util.date_format(exam_paper.limit_start_time),
        #                        datetime_util.date_format(exam_paper.limit_end_time)]
        #     vm.limit_date_time = limit_date_time

        return vo

    # result = ExamPaper.query.filter_by(subject_id=id_).first()
    # return Resp(1, "success", result.to_dict()).data()

    @staticmethod
    def page_list(paper_type, subject_id, page_index, page_size):
        query = ExamPaper.query
        if paper_type is not None:
            query = query.filter(ExamPaper.paper_type == paper_type)
        if subject_id is not None:
            query = query.filter(ExamPaper.subject_id == subject_id)
        pagination = query.paginate(page=page_index, per_page=page_size)
        papers = pagination.items
        result = {
            "list": [paper.to_dict() for paper in papers],
            "total": pagination.total,
            "PageNum": page_index
        }
        return result
