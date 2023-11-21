from sqlalchemy import Column, Integer, DateTime, Text
from dao.Database import db
import json


class TextContent(db.Model):
    __tablename__ = 't_text_content'

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=True)
    create_time = Column(DateTime, nullable=True)

    def __init__(self, content, create_time):
        self.content = content
        self.create_time = create_time
