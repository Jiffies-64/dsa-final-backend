from sqlalchemy import Column, Integer, DateTime
from dao.Database import db


class TaskExamCustomerAnswer(db.Model):
    __tablename__ = 't_task_exam_customer_answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_exam_id = Column(Integer, nullable=True)
    create_user = Column(Integer, nullable=True)
    create_time = Column(DateTime, nullable=True)
    text_content_id = Column(Integer, nullable=True)

    def __init__(self, task_exam_id, create_user, create_time, text_content_id):
        self.task_exam_id = task_exam_id
        self.create_user = create_user
        self.create_time = create_time
        self.text_content_id = text_content_id
