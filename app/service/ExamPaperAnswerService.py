import json
from datetime import datetime

from entity.po.ExamPaperAnswer import ExamPaperAnswer
from entity.po.ExamPaperQuestionCustomerAnswer import ExamPaperQuestionCustomerAnswer
from entity.vo.ExamPaperSubmitVo import ExamPaperSubmitVo, ExamPaperSubmitItemVo, ExamPaperAnswerPageResponseVo
from entity.vo.ExamPaperVo import ExamPaperEditRequestVo
from dao.Database import db
from service.SubjectService import SubjectService
from service.ExamPaperService import ExamPaperService
from service.TextContentService import TextContentService


class ExamPaperAnswerService:
    @staticmethod
    def request_to_exam_paper_submit_vm(id_, do_time, answer):
        exam_paper_submit_vm = ExamPaperSubmitVo()
        exam_paper_submit_vm.id = id_
        exam_paper_submit_vm.do_time = do_time

        answer_items = []
        for each in answer:
            exam_paper_submit_item_vm = ExamPaperSubmitItemVo()
            exam_paper_submit_item_vm.question_id = each['questionId']
            exam_paper_submit_item_vm.item_order = each['itemOrder']
            exam_paper_submit_item_vm.question_type_enum = each['questionTypeEnum']
            exam_paper_submit_item_vm.content = each['content']
            exam_paper_submit_item_vm.content_array = each['contentArray']
            answer_items.append(exam_paper_submit_item_vm)

        exam_paper_submit_vm.answer_items = answer_items
        return exam_paper_submit_vm
        # parameter_names = [name for name in request.args.keys() if "_" in name]
        #
        # # 题目答案按序号分组
        # question_group = {}
        # for parameter_name in parameter_names:
        #     key_parts = parameter_name.split('_')
        #     group_key = key_parts[0]
        #     if group_key not in question_group:
        #         question_group[group_key] = []
        #     question_group[group_key].append(parameter_name)

        # answer_items = []
        # for group_key, parameter_names in question_group.items():
        #     exam_paper_submit_item_vm = ExamPaperSubmitItemVM()
        #     parameter_name = parameter_names[0]
        #     keys = parameter_name.split('_')
        #     exam_paper_submit_item_vm.question_id = int(keys[1])
        #     exam_paper_submit_item_vm.item_order = int(keys[0])
        #     question_type_enum = QuestionTypeEnum(int(keys[2]))
        #
        #     if len(parameter_names) == 1:
        #         content = request.args.get(parameter_name)
        #         exam_paper_submit_item_vm.content = content
        #         if question_type_enum == QuestionTypeEnum.MultipleChoice:
        #             exam_paper_submit_item_vm.content_array = content.split(",")
        #     else:  # 多个空 填空题
        #         answers = [request.args.get(input_key) for input_key in sorted(parameter_names, key=last_num)]
        #         exam_paper_submit_item_vm.content_array = answers
        #
        #     answer_items.append(exam_paper_submit_item_vm)

    @staticmethod
    def submit(question_id, do_time, answer):
        time = str(datetime.now())
        exam_paper_submit_vo = ExamPaperAnswerService.request_to_exam_paper_submit_vm(question_id, do_time, answer)
        paper = ExamPaperService.select(exam_paper_submit_vo.id)
        exam_paper_answer = ExamPaperAnswer()

        exam_paper_answer.exam_paper_id = paper.id
        exam_paper_answer.paper_name = paper.name
        exam_paper_answer.paper_type = paper.paper_type
        exam_paper_answer.subject_id = paper.subject_id
        exam_paper_answer.question_count = len(exam_paper_submit_vo.answer_items)
        exam_paper_answer.do_time = exam_paper_submit_vo.do_time
        correct_count = 0
        system_score = 0
        question_customer_answer_text_lst = []
        for each in exam_paper_submit_vo.answer_items:
            q = paper.get_question_by_order(each.item_order)
            if q is not None:
                q_po = ExamPaperQuestionCustomerAnswer()
                q_po.question_id = q.id
                q_po.exam_paper_id = paper.id
                q_po.exam_paper_answer_id = paper.id
                q_po.question_type = q.question_type
                q_po.subject_id = q.subject_id
                q_po.question_score = q.score
                # q_po.question_text_content_id = -1
                # q_po.text_content_id = -1
                q_po.create_user = -1
                q_po.create_time = time
                q_po.item_order = each.item_order
                if q.question_type in (1, 3):
                    # q_po.answer = json.dumps(each.content)
                    q_po.answer = each.content
                    if q.correct == each.content:
                        q_po.customer_score = q.score
                        q_po.do_right = True
                        correct_count += 1
                        system_score += int(q.score)
                    else:
                        q_po.customer_score = 0
                        q_po.do_right = False
                elif q.question_type == 2:
                    q_po.answer = json.dumps(each.content_array)
                    # q_po.answer = each.content_array
                    if set(q.correct_array) == set(each.content_array):
                        q_po.customer_score = q.score
                        q_po.do_right = True
                        correct_count += 1
                        system_score += int(q.score)
                    else:
                        q_po.customer_score = 0
                        q_po.do_right = False
                else:
                    q_po.answer = each.content
                    q_po.customer_score = 0
                    q_po.do_right = False
                db.session.add(q_po)
                db.session.commit()
                question_customer_answer_text_lst.append(q_po.id)
        id_ = TextContentService.insert(question_customer_answer_text_lst)
        exam_paper_answer.question_customer_answer_text_content_id = id_
        exam_paper_answer.system_score = system_score
        exam_paper_answer.user_score = system_score
        exam_paper_answer.paper_score = paper.score
        exam_paper_answer.question_correct = correct_count
        exam_paper_answer.status = 1
        exam_paper_answer.create_time = time

        db.session.add(exam_paper_answer)
        db.session.commit()
        return exam_paper_answer.user_score

    @staticmethod
    def page_list(page_index, page_size):
        query = ExamPaperAnswer.query
        pagination = query.paginate(page=page_index, per_page=page_size)
        answers = pagination.items
        resp_lst = []
        for answer in answers:
            vo = ExamPaperAnswerPageResponseVo()
            vo.id = answer.id
            vo.create_time = answer.create_time
            vo.user_score = answer.user_score
            vo.subject_name = SubjectService.get_name_by_id(answer.subject_id)
            vo.subject_id = answer.subject_id
            vo.question_count = answer.question_count
            vo.question_correct = answer.question_correct
            vo.paper_score = answer.paper_score
            vo.do_time = answer.do_time
            vo.paper_type = answer.paper_type
            vo.system_score = answer.system_score
            vo.status = answer.status
            vo.paper_name = answer.paper_name
            vo.user_name = answer.create_user
            resp_lst.append(vo)
        result = {
            "list": [vo.to_dict() for vo in resp_lst],
            "total": pagination.total,
            "PageNum": page_index
        }
        return result

    # @staticmethod
    # def select(id_):
    #     answer = ExamPaperAnswer.query.filter_by(id=id_).first()
    #     vo = ExamPaperAnswerPageResponseVo()
    #     vo.id = answer.id
    #     vo.create_time = answer.create_time
    #     vo.user_score = answer.user_score
    #     vo.subject_name = SubjectService.get_name_by_id(answer.subject_id)
    #     vo.subject_id = answer.subject_id
    #     vo.question_count = answer.question_count
    #     vo.question_correct = answer.question_correct
    #     vo.paper_score = answer.paper_score
    #     vo.do_time = answer.do_time
    #     vo.paper_type = answer.paper_type
    #     vo.system_score = answer.system_score
    #     vo.status = answer.status
    #     vo.paper_name = answer.paper_name
    #     vo.user_name = answer.create_user
    #     return vo

    @staticmethod
    def po_to_exam_paper_submit_vo(id_):
        exam_paper_answer = ExamPaperAnswer.query.filter_by(id=id_).first()
        exam_paper_submit_vo = ExamPaperSubmitVo()
        exam_paper_submit_vo.id = exam_paper_answer.exam_paper_id
        exam_paper_submit_vo.do_time = exam_paper_answer.do_time

        answer_items = []
        question_customer_answer_id_lst = json.loads(TextContentService.select_by_id(exam_paper_answer.question_customer_answer_text_content_id).content)
        for id_ in question_customer_answer_id_lst:
            q_po = ExamPaperQuestionCustomerAnswer.query.filter_by(id=id_).first()
            exam_paper_submit_item_vo = ExamPaperSubmitItemVo()
            exam_paper_submit_item_vo.question_id = q_po.question_id
            exam_paper_submit_item_vo.item_order = q_po.item_order
            exam_paper_submit_item_vo.question_type_enum = q_po.question_type
            if q_po.question_type in (1, 3, 4, 5):
                exam_paper_submit_item_vo.content = q_po.answer
                exam_paper_submit_item_vo.content_array = []
            else:
                exam_paper_submit_item_vo.content = ""
                exam_paper_submit_item_vo.content_array = json.loads(q_po.answer)
            exam_paper_submit_item_vo.score = q_po.customer_score
            exam_paper_submit_item_vo.do_right = (q_po.customer_score != 0)
            exam_paper_submit_item_vo.question_score = q_po.question_score

            answer_items.append(exam_paper_submit_item_vo)

        exam_paper_submit_vo.answer_items = answer_items
        exam_paper_submit_vo.score = exam_paper_answer.system_score
        return exam_paper_submit_vo

    @staticmethod
    def read(id_):
        answer = ExamPaperAnswerService.po_to_exam_paper_submit_vo(id_)
        paper = ExamPaperService.select(answer.id)
        return {
            "paper": paper,
            "answer": answer.to_json()
        }
