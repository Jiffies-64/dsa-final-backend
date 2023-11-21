from dao.Database import db
from entity.po.User import User
from entity.vo.Resp import Resp
from utils.Passwd import PasswordHasher
from utils.UUID import UUIDGenerator


class StudentService:

    @staticmethod
    def create_stu(user_name, password, user_level):
        init_data = {
            "user_uuid": UUIDGenerator.generate_uuid_from_string(user_name),
            "user_name": user_name,
            "password": PasswordHasher.hash_password(password),
            "user_level": user_level
        }
        user = User(**init_data)
        db.session.add(user)
        db.session.commit()
        return Resp(1, "注册成功", None).data()

    @staticmethod
    def get_current_user_info(user_name):
        if user_name is None:
            return Resp(2, "用户未登录", {'imagePath': None}).data()
        user = User.query.filter_by(user_name=user_name).first()
        return Resp(1, "success", {'imagePath': user.image_path}).data()

    @staticmethod
    def get_user_event():
        # 获取用户事件逻辑
        # 这里可以查询用户的事件日志等
        pass

    @staticmethod
    def update_user(user_id, update_data):
        # 更新用户逻辑
        user = User.query.get(user_id)
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        else:
            return None

    @staticmethod
    def get_message_page_list(query):
        # 获取用户消息分页列表逻辑
        # 这里可以查询用户的消息分页列表
        pass

    @staticmethod
    def mark_message_as_read(message_id):
        # 将消息标记为已读逻辑
        # 根据message_id更新消息的状态为已读
        pass

    @staticmethod
    def get_message_count():
        # 获取用户未读消息数量逻辑
        # 这里可以查询用户的未读消息数量
        pass
