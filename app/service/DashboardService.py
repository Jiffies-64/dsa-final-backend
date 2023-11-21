from dao.Database import db
from entity.po.User import User
from utils.Passwd import PasswordHasher
from utils.UUID import UUIDGenerator


class DashboardService:

    @staticmethod
    def index():
        # _this.fixedPaper = re.response.fixedPaper
        # _this.timeLimitPaper = re.response.timeLimitPaper
        # _this.pushPaper = re.response.pushPaper
        return None

    @staticmethod
    def get_current_user_info(user_name):
        if user_name is None:
            return {'imagePath': None}
        user = User.query.filter_by(user_name=user_name).first()
        return {'imagePath': user.image_path}
