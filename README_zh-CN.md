# DSA-FINAL-BACKEND

2023年数据科学应用方向实践项目



## 环境配置

**① 运行数据库脚本**

数据库脚本位于项目根目录

**② 配置app目录下`.env`文件**

具体字段解释如下：

| 字段           | 说明                            |
| -------------- | ------------------------------- |
| DB_HOSTNAME    | mysql数据库ip                   |
| DB_PORT        | mysql数据库端口                 |
| DB_USERNAME    | mysql数据库用户名               |
| DB_PASSWORD    | mysql数据库密码                 |
| DB_DATABASE    | mysql数据库名                   |
| OFFLOAD_FOLDER | 模型参数卸载路径                |
| HF_HOME        | 从huggingface下载的模型存放路径 |

*注意：从huggingface下载模型可能需要科学上网



## 运行

配置完成后，即可通过 `python app/app.py` 启动后端服务器