from sqlalchemy import Column, Integer, String, Boolean
from dao.Database import db


class Subject(db.Model):
    __tablename__ = 't_subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    level = Column(Integer, nullable=True)
    level_name = Column(String(255), nullable=True)
    item_order = Column(Integer, nullable=True)
    deleted = Column(Boolean, nullable=True)

    def __init__(self, name, level, level_name, item_order, deleted):
        self.name = name
        self.level = level
        self.level_name = level_name
        self.item_order = item_order
        self.deleted = deleted

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'level_name': self.level_name,
            'item_order': self.item_order,
            'deleted': self.deleted
        }
