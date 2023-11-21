[TOC]

# DSA-FINAL-BACKEND

2023 xxxx xxxx



## 环境配置

设置环境变量`HF_HOME`用以指定存放huggingface模型的路径

`app/models/models.py`文件`init_model(self)`函数中`offload_folder`指定模型参数卸载路径

mysql：脚本位于本项目根目录


## 目录结构

来自ChatGPT

```
arduinoCopy codemyflaskapp/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── main.py
│   │   ├── api.py
│   │   └── ...
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   │   └── ...
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── ...
│   ├── config.py
│   └── ...
│
├── migrations/
│
├── tests/
│
├── instance/
│   └── config.py
│
├── venv/
│
├── run.py
│
├── requirements.txt
│
└── .gitignore
```

以下是各个目录的主要作用：

- `app/`: 包含应用程序的核心代码，包括路由、模型、模板、静态文件等。
  - `routes/`: 包含路由视图函数，通常按功能或模块划分。
  - `models/`: 包含应用程序的数据模型，通常对数据库表进行建模。
  - `templates/`: 包含HTML模板文件，用于渲染视图。
  - `static/`: 包含静态文件，如CSS、JavaScript和图像。
  - `config.py`: 包含应用程序的配置参数。
- `migrations/`: 包含数据库迁移文件，用于数据库模式的升级和降级。
- `tests/`: 包含应用程序的测试代码。
- `instance/`: 包含实例配置文件，通常用于存储应用程序的敏感信息，如密钥。
- `venv/`: 包含虚拟环境，用于隔离项目依赖。
- `run.py`: 项目的入口点，用于启动应用程序。
- `requirements.txt`: 包含项目的依赖项列表，可通过`pip install -r requirements.txt`来安装依赖。
- `.gitignore`: 指定要忽略的文件和目录，通常包括虚拟环境、数据库文件和敏感信息。

