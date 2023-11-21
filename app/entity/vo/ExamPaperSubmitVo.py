# 提交试卷时具体每一道题
class ExamPaperSubmitItemVo:
    question_id: int
    do_right: bool
    content: str
    item_order: int
    content_array: []
    score: int
    question_score: int

    def init_from_json(self, json_data: dict):
        self.question_id = json_data.get('questionId')
        self.do_right = json_data.get('doRight')
        self.content = json_data.get('content')
        self.item_order = json_data.get('itemOrder')
        self.content_array = json_data.get('contentArray')
        self.score = json_data.get('score')
        self.question_score = json_data.get('questionScore')

    def to_json(self):
        return {
            "questionId": self.question_id,
            "doRight": self.do_right,
            "content": self.content,
            "itemOrder": self.item_order,
            "contentArray": self.content_array,
            "score": self.score,
            "questionScore": self.question_score
        }


# 提交的试卷详细信息
class ExamPaperSubmitVo:
    id: int
    do_time: int
    score: int
    answer_items: []

    def init_from_json(self, json_data: dict):
        self.id = json_data.get('id')
        self.do_time = json_data.get('doTime')
        self.score = json_data.get('score')
        answer_items_data = json_data.get('answerItems', [])
        self.answer_items = [ExamPaperSubmitItemVo(item_data) for item_data in answer_items_data]

    def to_json(self):
        return {
            "id": self.id,
            "doTime": self.do_time,
            "score": self.score,
            "answerItems": [item.to_json() for item in self.answer_items]
        }


# 试卷整体内容
class ExamPaperAnswerPageResponseVo:
    def __init__(self):
        self.id = None
        self.create_time = None
        self.user_score = None
        self.subject_name = None
        self.subject_id = None
        self.question_count = None
        self.question_correct = None
        self.paper_score = None
        self.do_time = None
        self.paper_type = None
        self.system_score = None
        self.status = None
        self.paper_name = None
        self.user_name = None

    def to_dict(self):
        return {
            'id': self.id,
            'createTime': self.create_time,
            'userScore': self.user_score,
            'subjectName': self.subject_name,
            'subjectId': self.subject_id,
            'questionCount': self.question_count,
            'questionCorrect': self.question_correct,
            'paperScore': self.paper_score,
            'doTime': self.do_time,
            'paperType': self.paper_type,
            'systemScore': self.system_score,
            'status': self.status,
            'paperName': self.paper_name,
            'userName': self.user_name,
        }
