from sqlalchemy import Column, Integer, String, DateTime
from dao.Database import db


class ExamPaperAnswer(db.Model):
    __tablename__ = 't_exam_paper_answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 试卷id
    exam_paper_id = Column(Integer, nullable=True)
    # 试卷名称
    paper_name = Column(String(255), nullable=True)
    # 试卷类型( 1.固定试卷 4.时段试卷 6.任务试卷)
    paper_type = Column(Integer, nullable=True)
    # 学科
    subject_id = Column(Integer, nullable=True)
    # 系统判定得分
    system_score = Column(Integer, nullable=True)
    # 最终得分(千分制)
    user_score = Column(Integer, nullable=True)
    # 试卷总分
    paper_score = Column(Integer, nullable=True)
    # 做对题目数量
    question_correct = Column(Integer, nullable=True)
    # 题目总数量
    question_count = Column(Integer, nullable=True)
    # 做题时间(秒)
    do_time = Column(Integer, nullable=True)
    # 试卷状态(1待判分 2完成)
    status = Column(Integer, nullable=True)
    # 学生
    create_user = Column(Integer, nullable=True)
    # 提交时间
    create_time = Column(DateTime, nullable=True)
    # 记录用户做题内容
    question_customer_answer_text_content_id = Column(Integer, nullable=True)

    def init_by(self, exam_paper_id, paper_name, paper_type, subject_id, system_score, user_score,
                 paper_score, question_correct, question_count, do_time, status, create_user,
                 create_time, question_customer_answer_text_content_id):
        self.exam_paper_id = exam_paper_id
        self.paper_name = paper_name
        self.paper_type = paper_type
        self.subject_id = subject_id
        self.system_score = system_score
        self.user_score = user_score
        self.paper_score = paper_score
        self.question_correct = question_correct
        self.question_count = question_count
        self.do_time = do_time

    def to_dict(self):
        return {
            'id': self.id,
            'exam_paper_id': self.exam_paper_id,
            'paper_name': self.paper_name,
            'paper_type': self.paper_type,
            'subject_id': self.subject_id,
            'system_score': self.system_score,
            'user_score': self.user_score,
            'paper_score': self.paper_score,
            'question_correct': self.question_correct,
            'question_count': self.question_count,
            'do_time': self.do_time,
            'status': self.status,
            'create_user': self.create_user,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None,
            'question_customer_answer_text_content_id': self.question_customer_answer_text_content_id
        }
