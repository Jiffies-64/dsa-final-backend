from flask import Flask, render_template
from dao.Database import db
from utils.Env import DB_HOSTNAME, DB_DATABASE, DB_USERNAME, DB_PASSWORD, DB_PORT
from controller.UserController import UserController
from controller.StudentController import StudentController
from controller.DashboardController import DashboardController
from controller.SubjectController import SubjectController
from controller.ExamPaperController import ExamPaperController
from controller.ExamPaperAnswerController import ExamPaperAnswerController
from controller.QuestionAnswerController import QuestionAnswerController
from controller.ChatController import socketio

app = Flask(__name__, template_folder="./templates")
app.config['SQLALCHEMY_DATABASE_URI'] \
    = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"
db.init_app(app)
socketio.init_app(app)

# with app.app_context():
#     db.create_all()


app.register_blueprint(UserController, url_prefix='/api/user')
app.register_blueprint(StudentController, url_prefix='/api/student/user')
app.register_blueprint(DashboardController, url_prefix='/api/student/dashboard')
app.register_blueprint(SubjectController, url_prefix='/api/student/education/subject')
app.register_blueprint(ExamPaperController, url_prefix='/api/student/exam/paper')
app.register_blueprint(ExamPaperAnswerController, url_prefix='/api/student/exampaper/answer')
app.register_blueprint(QuestionAnswerController, url_prefix='/api/student/question/answer')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=8000, debug=True)
    socketio.run(app, host="127.0.0.1", port=8000, debug=False)
