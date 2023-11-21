import json

from sqlalchemy import Column, Integer, Text, DateTime, Boolean
from dao.Database import db


class Question(db.Model):
    __tablename__ = 't_question'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 1.单选题 2.多选题 3.判断题 4.填空题 5.简答题
    question_type = Column(Integer, nullable=True)
    # 学科
    subject_id = Column(Integer, nullable=True)
    # 题目总分(千分制)
    score = Column(Integer, nullable=True)
    # 级别
    grade_level = Column(Integer, nullable=True)
    # 难度
    difficult = Column(Integer, nullable=True)
    # 正确答案
    correct = Column(Text, nullable=True)
    # 题目 填空、题干、解析、答案等信息
    info_text_content_id = Column(Integer, nullable=True)
    # 创建者
    create_user = Column(Integer, nullable=True)
    # 1.正常
    status = Column(Integer, nullable=True)
    # 创建时间
    create_time = Column(DateTime, nullable=True)
    # 是否删除
    deleted = Column(Boolean, nullable=True)

    def __init__(self, question_type, subject_id, score, grade_level, difficult, correct,
                 info_text_content_id, create_user, status, create_time, deleted):
        self.question_type = question_type
        self.subject_id = subject_id
        self.score = score
        self.grade_level = grade_level
        self.difficult = difficult
        self.correct = correct
        self.info_text_content_id = info_text_content_id
        self.create_user = create_user
        self.status = status
        self.create_time = create_time
        self.deleted = deleted
