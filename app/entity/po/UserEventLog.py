from sqlalchemy import Column, Integer, String, DateTime, Text
from dao.Database import db


class UserEventLog(db.Model):
    __tablename__ = 't_user_event_log'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    user_name = Column(String(255), nullable=True)
    real_name = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    create_time = Column(DateTime, nullable=True)

    def __init__(self, user_id, user_name, real_name, content, create_time):
        self.user_id = user_id
        self.user_name = user_name
        self.real_name = real_name
        self.content = content
        self.create_time = create_time
