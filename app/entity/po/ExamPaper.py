from sqlalchemy import Column, Integer, String, DateTime, Boolean
from dao.Database import db


class ExamPaper(db.Model):
    __tablename__ = 't_exam_paper'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    subject_id = Column(Integer, nullable=True)
    paper_type = Column(Integer, nullable=True)
    grade_level = Column(Integer, nullable=True)
    score = Column(Integer, nullable=True)
    question_count = Column(Integer, nullable=True)
    suggest_time = Column(Integer, nullable=True)
    limit_start_time = Column(DateTime, nullable=True)
    limit_end_time = Column(DateTime, nullable=True)
    frame_text_content_id = Column(Integer, nullable=True)
    create_user = Column(Integer, nullable=True)
    create_time = Column(DateTime, nullable=True)
    deleted = Column(Boolean, nullable=True)
    task_exam_id = Column(Integer, nullable=True)

    def __init__(self, name, subject_id, paper_type, grade_level, score, question_count, suggest_time,
                 limit_start_time, limit_end_time, frame_text_content_id, create_user, create_time,
                 deleted, task_exam_id):
        self.name = name
        self.subject_id = subject_id
        self.paper_type = paper_type
        self.grade_level = grade_level
        self.score = score
        self.question_count = question_count
        self.suggest_time = suggest_time
        self.limit_start_time = limit_start_time
        self.limit_end_time = limit_end_time
        self.frame_text_content_id = frame_text_content_id
        self.create_user = create_user
        self.create_time = create_time
        self.deleted = deleted
        self.task_exam_id = task_exam_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'subject_id': self.subject_id,
            'paper_type': self.paper_type,
            'grade_level': self.grade_level,
            'score': self.score,
            'question_count': self.question_count,
            'suggest_time': self.suggest_time,
            'limit_start_time': self.limit_start_time.strftime('%Y-%m-%d %H:%M:%S') if self.limit_start_time else None,
            'limit_end_time': self.limit_end_time.strftime('%Y-%m-%d %H:%M:%S') if self.limit_end_time else None,
            'frame_text_content_id': self.frame_text_content_id,
            'create_user': self.create_user,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else None,
            'deleted': self.deleted,
            'task_exam_id': self.task_exam_id
        }
