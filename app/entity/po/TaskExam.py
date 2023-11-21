from sqlalchemy import Column, Integer, String, DateTime, Boolean
from dao.Database import db


class TaskExam(db.Model):
    __tablename__ = 't_task_exam'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    grade_level = Column(Integer, nullable=True)
    frame_text_content_id = Column(Integer, nullable=True)
    create_user = Column(Integer, nullable=True)
    create_time = Column(DateTime, nullable=True)
    deleted = Column(Boolean, nullable=True)
    create_user_name = Column(String(255), nullable=True)

    def __init__(self, title, grade_level, frame_text_content_id, create_user, create_time,
                 deleted, create_user_name):
        self.title = title
        self.grade_level = grade_level
        self.frame_text_content_id = frame_text_content_id
        self.create_user = create_user
        self.create_time = create_time
        self.deleted = deleted
        self.create_user_name = create_user_name
