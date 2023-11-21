from datetime import datetime

from entity.po.TextContent import TextContent
import json
from dao.Database import db


class TextContentService:

    @staticmethod
    def select_by_id(id_):
        return TextContent.query.filter_by(id=id_).first()

    @staticmethod
    def get_content_class_by_id(id_, clazz):
        text_content = TextContentService.select_by_id(id_)
        if text_content is None:
            return None
        return clazz.from_json(text_content.content)

    @staticmethod
    def insert(content):
        now = str(datetime.now())
        tc = TextContent(json.dumps(content), now)
        db.session.add(tc)
        db.session.commit()
        return tc.id


class QuestionObject:
    def __init__(self, titleContent, analyze, questionItemObjects, correct):
        self.titleContent = titleContent
        self.analyze = analyze
        self.questionItemObjects = questionItemObjects
        self.correct = correct

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        if 'questionItemObjects' not in data.keys():
            questionItemObjects = []
        else:
            questionItemObjects = data['questionItemObjects']
        return cls(
            titleContent=data['titleContent'],
            analyze=data['analyze'],
            questionItemObjects=questionItemObjects,
            correct=data['correct']
        )

    def to_json(self):
        return json.dumps(self.__dict__)


class QuestionItemObject:
    def __init__(self, prefix, content, score, itemUuid):
        self.prefix = prefix
        self.content = content
        self.score = score
        self.itemUuid = itemUuid

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(
            prefix=data['prefix'],
            content=data['content'],
            score=data['score'],
            itemUuid=data['itemUuid']
        )

    def to_json(self):
        return json.dumps(self.__dict__)
