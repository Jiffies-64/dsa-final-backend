from sqlalchemy import Column, Integer, String, DateTime, Boolean
from dao.Database import db


class User(db.Model):
    __tablename__ = 't_user'

    # 主鍵
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 用户 UUID
    user_uuid = Column(String(36), nullable=True)
    # 用户名
    user_name = Column(String(255), nullable=False)
    # 密码
    password = Column(String(255), nullable=False)
    # 真实姓名
    real_name = Column(String(255), nullable=True)
    # 年龄
    age = Column(Integer, nullable=True)
    # 性别
    sex = Column(Integer, nullable=True)
    # 出生日期
    birth_day = Column(DateTime, nullable=True)
    # 用户级别
    user_level = Column(Integer, nullable=True)
    # 电话号码
    phone = Column(String(255), nullable=True)
    # 角色
    role = Column(Integer, nullable=True)
    # 状态
    status = Column(Integer, nullable=True)
    # 头像路径
    image_path = Column(String(255), nullable=True)
    # 创建时间
    create_time = Column(DateTime, nullable=True)
    # 修改时间
    modify_time = Column(DateTime, nullable=True)
    # 最后活动时间
    last_active_time = Column(DateTime, nullable=True)
    # 删除标志
    deleted = Column(Boolean, nullable=True)
    # 微信 Open ID
    wx_open_id = Column(String(255), nullable=True)
