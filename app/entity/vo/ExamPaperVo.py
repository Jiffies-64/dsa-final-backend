# 该类相当于整张试卷
class ExamPaperEditRequestVo:
    id: int
    level: int
    subject_id: int
    paper_type: int
    name: str
    suggest_time: int
    limit_date_time: [str]
    title_items: []
    score: str

    # def init_from_exam_paper(self, exam_paper):
    #     self.id = exam_paper.id
    #     self.level = exam_paper.grade_level
    #     self.subject_id = exam_paper.subject_id
    #     self.paper_type = exam_paper.paper_type
    #     self.name = exam_paper.name
    #     self.suggest_time = exam_paper.suggest_time
    #     self.limit_date_time = [
    #         exam_paper.limit_start_time.strftime('%Y-%m-%d %H:%M:%S') if exam_paper.limit_start_time else None,
    #         exam_paper.limit_end_time.strftime('%Y-%m-%d %H:%M:%S') if exam_paper.limit_end_time else None
    #     ]
    #     self.score = str(exam_paper.score)

    # def set_title_items(self, lst):
    #     self.title_items = lst

    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'subjectId': self.subject_id,
            'paperType': self.paper_type,
            'name': self.name,
            'suggestTime': self.suggest_time,
            'limitDateTime': self.limit_date_time,
            'titleItems': [each.to_dict() for each in self.title_items],
            'score': self.score
        }

    def get_question_by_order(self, order):
        for title in self.title_items:
            for q in title.question_items:
                if q.item_order == order:
                    return q
        return None


# 该类相当于试卷的章节，如选择题部分、填空题部分（不限于按题目类型划分）
class ExamPaperTitleItemVo:
    name: str
    question_items: []

    def to_dict(self):
        return {
            'name': self.name,
            'questionItems': [each.to_dict() for each in self.question_items]
        }


# 该类相当于单个题目，可以有五种类型：1.单选题 2.多选题 3.判断题 4.填空题 5.简答题
class QuestionEditRequestVo:
    id: int
    question_type: int
    subject_id: int
    title: str
    grade_level: int
    items: []
    analyze: str
    correct_array = []
    correct = ''
    score: str
    difficult: int
    item_order: int

    # def init(self, question_po, question_object):
    #     # from question
    #     self.id = question_po.id
    #     self.question_type = question_po.question_type
    #     self.subject_id = question_po.subject_id
    #     self.grade_level = question_po.grade_level
    #     self.score = str(question_po.score)  # 转换为字符串，根据实际需要进行调整
    #     self.difficult = question_po.difficult
    #     # from dict
    #     self.title = question_object.titleContent
    #     self.analyze = question_object.analyze
    #     if self.question_type in (1, 3):
    #         # 单选、判断
    #         self.correct = question_object.correct
    #     elif self.question_type == 2:
    #         # 多选
    #         self.correct_array = question_object.correct
    #     elif self.question_type == 4:
    #         # 填空
    #         self.correct_array = question_object.correct
    #     else:
    #         # 问答
    #         self.correct = question_object.correct
    #     # from items
    #     self.items = question_object.questionItemObjects

    def to_dict(self):
        return {
            'id': self.id,
            'questionType': self.question_type,
            'subjectId': self.subject_id,
            'title': self.title,
            'gradeLevel': self.grade_level,
            'items': self.items,
            'analyze': self.analyze,
            'correct': self.correct,
            'correctArray': self.correct_array,
            'score': self.score,
            'difficult': self.difficult,
            'itemOrder': self.item_order
        }


# 该类相当于具体选项及分值
class QuestionEditItemVo:
    prefix: str
    content: str
    score: str
    item_uuid: str

    def to_dict(self):
        return {
            "prefix": self.prefix,
            "content": self.content,
            "score": self.score,
            "item_uuid": self.item_uuid
        }
