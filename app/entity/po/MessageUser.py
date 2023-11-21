from sqlalchemy import Column, Integer, String, DateTime, Boolean
from dao.Database import db


class MessageUser(db.Model):
    __tablename__ = 't_message_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(Integer, nullable=True)
    receive_user_id = Column(Integer, nullable=True)
    receive_user_name = Column(String(255), nullable=True)
    receive_real_name = Column(String(255), nullable=True)
    readed = Column(Boolean, nullable=True)
    create_time = Column(DateTime, nullable=True)
    read_time = Column(DateTime, nullable=True)

    def __init__(self, message_id, receive_user_id, receive_user_name, receive_real_name,
                 readed, create_time, read_time):
        self.message_id = message_id
        self.receive_user_id = receive_user_id
        self.receive_user_name = receive_user_name
        self.receive_real_name = receive_real_name
        self.readed = readed
        self.create_time = create_time
        self.read_time = read_time
