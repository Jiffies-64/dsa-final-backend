from sqlalchemy import Column, Integer, String, DateTime, Boolean
from dao.Database import db


class ExamPaperQuestionCustomerAnswer(db.Model):
    __tablename__ = 't_exam_paper_question_customer_answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 题目Id
    question_id = Column(Integer, nullable=True)
    # 试卷Id
    exam_paper_id = Column(Integer, nullable=True)
    # 答案Id
    exam_paper_answer_id = Column(Integer, nullable=True)
    # 题型
    question_type = Column(Integer, nullable=True)
    # 学科
    subject_id = Column(Integer, nullable=True)
    # 得分
    customer_score = Column(Integer, nullable=True)
    # 题目原始分数
    question_score = Column(Integer, nullable=True)
    # 问题内容(x
    question_text_content_id = Column(Integer, nullable=True)
    # 做题答案
    answer = Column(String(255), nullable=True)
    # 做题内容(x
    text_content_id = Column(Integer, nullable=True)
    # 是否正确
    do_right = Column(Boolean, nullable=True)
    create_user = Column(Integer, nullable=True)
    create_time = Column(DateTime, nullable=True)
    item_order = Column(Integer, nullable=True)

    def init_by(self, question_id, exam_paper_id, exam_paper_answer_id, question_type, subject_id,
                 customer_score, question_score, question_text_content_id, answer, text_content_id,
                 do_right, create_user, create_time, item_order):
        self.question_id = question_id
        self.exam_paper_id = exam_paper_id
        self.exam_paper_answer_id = exam_paper_answer_id
        self.question_type = question_type
        self.subject_id = subject_id
        self.customer_score = customer_score
        self.question_score = question_score
        self.question_text_content_id = question_text_content_id
        self.answer = answer
        self.text_content_id = text_content_id
        self.do_right = do_right
        self.create_user = create_user
        self.create_time = create_time
        self.item_order = item_order
