from sqlalchemy import Column, Integer, String, DateTime
from dao.Database import db


class Message(db.Model):
    __tablename__ = 't_message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    content = Column(String(500), nullable=True)
    create_time = Column(DateTime, nullable=True)
    send_user_id = Column(Integer, nullable=True)
    send_user_name = Column(String(255), nullable=True)
    send_real_name = Column(String(255), nullable=True)
    receive_user_count = Column(Integer, nullable=True)
    read_count = Column(Integer, nullable=True)

    def __init__(self, title, content, create_time, send_user_id, send_user_name,
                 send_real_name, receive_user_count, read_count):
        self.title = title
        self.content = content
        self.create_time = create_time
        self.send_user_id = send_user_id
        self.send_user_name = send_user_name
        self.send_real_name = send_real_name
        self.receive_user_count = receive_user_count
        self.read_count = read_count
