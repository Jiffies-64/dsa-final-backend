# DSA-FINAL-PACKEND

2023 Data Science Application Practice Project



## Environmental configuration

**① Run database scripts**

The database script is located in the project root directory

**② Configure the '. env' file in the app directory**

The specific field explanations are as follows:

| Field            | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| DB_ HOSTNAME     | MySQL database IP                                           |
| DB_ PORT         | MySQL database port                                         |
| DB_ USERNAME     | MySQL database username                                     |
| DB_ PASSWORD     | MySQL database password                                     |
| DB_ DATABASE     | MySQL database name                                         |
| OFF LOAD_ FOLDER | Model parameter unloading path                              |
| HF_ HOME         | The path to store the model downloaded from the huggingface |


## Run

After configuration is completed, you can start the backend server through the `python app/app.py`