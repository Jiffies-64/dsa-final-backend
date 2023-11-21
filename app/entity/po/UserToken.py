from sqlalchemy import Column, Integer, String, DateTime
from dao.Database import db


class UserToken(db.Model):
    __tablename__ = 't_user_token'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(36), nullable=True)
    user_id = Column(Integer, nullable=True)
    wx_open_id = Column(String(255), nullable=True)
    create_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    user_name = Column(String(255), nullable=True)

    def __init__(self, token, user_id, wx_open_id, create_time, end_time, user_name):
        self.token = token
        self.user_id = user_id
        self.wx_open_id = wx_open_id
        self.create_time = create_time
        self.end_time = end_time
        self.user_name = user_name
