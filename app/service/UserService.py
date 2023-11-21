from dao.Database import db
from entity.po.User import User
from entity.vo.Resp import Resp
from utils.Passwd import PasswordHasher


class UserService:

    @staticmethod
    def login(user_name, password):
        if not user_name or not password:
            return Resp(2, "用户名或密码不能为空", None).data()

        account = User.query.filter_by(user_name=user_name).first()
        if not account or not PasswordHasher.check_password(password, account.password):
            return Resp(2, "用户名或密码不正确", None).data()

        return Resp(1, "登录成功", None).data()

    @staticmethod
    def logout():
        return Resp(1, "登出成功", None).data()
