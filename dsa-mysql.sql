SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_exam_paper
-- ----------------------------
DROP TABLE IF EXISTS `t_exam_paper`;
CREATE TABLE `t_exam_paper`
(
    `id`                    int                                                           NOT NULL AUTO_INCREMENT,
    `name`                  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `subject_id`            int                                                           NULL DEFAULT NULL,
    `paper_type`            int                                                           NULL DEFAULT NULL,
    `grade_level`           int                                                           NULL DEFAULT NULL,
    `score`                 int                                                           NULL DEFAULT NULL,
    `question_count`        int                                                           NULL DEFAULT NULL,
    `suggest_time`          int                                                           NULL DEFAULT NULL,
    `limit_start_time`      datetime                                                      NULL DEFAULT NULL,
    `limit_end_time`        datetime                                                      NULL DEFAULT NULL,
    `frame_text_content_id` int                                                           NULL DEFAULT NULL,
    `create_user`           int                                                           NULL DEFAULT NULL,
    `create_time`           datetime                                                      NULL DEFAULT NULL,
    `deleted`               bit(1)                                                        NULL DEFAULT NULL,
    `task_exam_id`          int                                                           NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_exam_paper
-- ----------------------------

-- ----------------------------
-- Table structure for t_exam_paper_answer
-- ----------------------------
DROP TABLE IF EXISTS `t_exam_paper_answer`;
CREATE TABLE `t_exam_paper_answer`
(
    `id`                                       int                                                           NOT NULL AUTO_INCREMENT,
    `exam_paper_id`                            int                                                           NULL DEFAULT NULL,
    `paper_name`                               varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `paper_type`                               int                                                           NULL DEFAULT NULL,
    `subject_id`                               int                                                           NULL DEFAULT NULL,
    `system_score`                             int                                                           NULL DEFAULT NULL,
    `user_score`                               int                                                           NULL DEFAULT NULL,
    `paper_score`                              int                                                           NULL DEFAULT NULL,
    `question_correct`                         int                                                           NULL DEFAULT NULL,
    `question_count`                           int                                                           NULL DEFAULT NULL,
    `do_time`                                  int                                                           NULL DEFAULT NULL,
    `status`                                   int                                                           NULL DEFAULT NULL,
    `create_user`                              int                                                           NULL DEFAULT NULL,
    `create_time`                              datetime                                                      NULL DEFAULT NULL,
    `question_customer_answer_text_content_id` int                                                           NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_exam_paper_answer
-- ----------------------------

-- ----------------------------
-- Table structure for t_exam_paper_question_customer_answer
-- ----------------------------
DROP TABLE IF EXISTS `t_exam_paper_question_customer_answer`;
CREATE TABLE `t_exam_paper_question_customer_answer`
(
    `id`                       int                                                           NOT NULL AUTO_INCREMENT,
    `question_id`              int                                                           NULL DEFAULT NULL,
    `exam_paper_id`            int                                                           NULL DEFAULT NULL,
    `exam_paper_answer_id`     int                                                           NULL DEFAULT NULL,
    `question_type`            int                                                           NULL DEFAULT NULL,
    `subject_id`               int                                                           NULL DEFAULT NULL,
    `customer_score`           int                                                           NULL DEFAULT NULL,
    `question_score`           int                                                           NULL DEFAULT NULL,
    `question_text_content_id` int                                                           NULL DEFAULT NULL,
    `answer`                   varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `text_content_id`          int                                                           NULL DEFAULT NULL,
    `do_right`                 bit(1)                                                        NULL DEFAULT NULL,
    `create_user`              int                                                           NULL DEFAULT NULL,
    `create_time`              datetime                                                      NULL DEFAULT NULL,
    `item_order`               int                                                           NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_exam_paper_question_customer_answer
-- ----------------------------

-- ----------------------------
-- Table structure for t_message
-- ----------------------------
DROP TABLE IF EXISTS `t_message`;
CREATE TABLE `t_message`
(
    `id`                 int                                                           NOT NULL AUTO_INCREMENT,
    `title`              varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `content`            varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `create_time`        datetime                                                      NULL DEFAULT NULL,
    `send_user_id`       int                                                           NULL DEFAULT NULL,
    `send_user_name`     varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `send_real_name`     varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `receive_user_count` int                                                           NULL DEFAULT NULL,
    `read_count`         int                                                           NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_message
-- ----------------------------

-- ----------------------------
-- Table structure for t_message_user
-- ----------------------------
DROP TABLE IF EXISTS `t_message_user`;
CREATE TABLE `t_message_user`
(
    `id`                int                                                           NOT NULL AUTO_INCREMENT,
    `message_id`        int                                                           NULL DEFAULT NULL,
    `receive_user_id`   int                                                           NULL DEFAULT NULL,
    `receive_user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `receive_real_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `readed`            bit(1)                                                        NULL DEFAULT NULL,
    `create_time`       datetime                                                      NULL DEFAULT NULL,
    `read_time`         datetime                                                      NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_message_user
-- ----------------------------

-- ----------------------------
-- Table structure for t_question
-- ----------------------------
DROP TABLE IF EXISTS `t_question`;
CREATE TABLE `t_question`
(
    `id`                   int                                                   NOT NULL AUTO_INCREMENT,
    `question_type`        int                                                   NULL DEFAULT NULL,
    `subject_id`           int                                                   NULL DEFAULT NULL,
    `score`                int                                                   NULL DEFAULT NULL,
    `grade_level`          int                                                   NULL DEFAULT NULL,
    `difficult`            int                                                   NULL DEFAULT NULL,
    `correct`              text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
    `info_text_content_id` int                                                   NULL DEFAULT NULL,
    `create_user`          int                                                   NULL DEFAULT NULL,
    `status`               int                                                   NULL DEFAULT NULL,
    `create_time`          datetime                                              NULL DEFAULT NULL,
    `deleted`              bit(1)                                                NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_question
-- ----------------------------

-- ----------------------------
-- Table structure for t_subject
-- ----------------------------
DROP TABLE IF EXISTS `t_subject`;
CREATE TABLE `t_subject`
(
    `id`         int                                                           NOT NULL AUTO_INCREMENT,
    `name`       varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `level`      int                                                           NULL DEFAULT NULL,
    `level_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `item_order` int                                                           NULL DEFAULT NULL,
    `deleted`    bit(1)                                                        NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_subject
-- ----------------------------

-- ----------------------------
-- Table structure for t_task_exam
-- ----------------------------
DROP TABLE IF EXISTS `t_task_exam`;
CREATE TABLE `t_task_exam`
(
    `id`                    int                                                           NOT NULL AUTO_INCREMENT,
    `title`                 varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `grade_level`           int                                                           NULL DEFAULT NULL,
    `frame_text_content_id` int                                                           NULL DEFAULT NULL,
    `create_user`           int                                                           NULL DEFAULT NULL,
    `create_time`           datetime                                                      NULL DEFAULT NULL,
    `deleted`               bit(1)                                                        NULL DEFAULT NULL,
    `create_user_name`      varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_task_exam
-- ----------------------------

-- ----------------------------
-- Table structure for t_task_exam_customer_answer
-- ----------------------------
DROP TABLE IF EXISTS `t_task_exam_customer_answer`;
CREATE TABLE `t_task_exam_customer_answer`
(
    `id`              int      NOT NULL AUTO_INCREMENT,
    `task_exam_id`    int      NULL DEFAULT NULL,
    `create_user`     int      NULL DEFAULT NULL,
    `create_time`     datetime NULL DEFAULT NULL,
    `text_content_id` int      NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_task_exam_customer_answer
-- ----------------------------

-- ----------------------------
-- Table structure for t_text_content
-- ----------------------------
DROP TABLE IF EXISTS `t_text_content`;
CREATE TABLE `t_text_content`
(
    `id`          int                                                   NOT NULL AUTO_INCREMENT,
    `content`     text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
    `create_time` datetime                                              NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_text_content
-- ----------------------------

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`
(
    `id`               int                                                           NOT NULL AUTO_INCREMENT,
    `user_uuid`        varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci  NULL DEFAULT NULL,
    `user_name`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `password`         varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `real_name`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `age`              int                                                           NULL DEFAULT NULL,
    `sex`              int                                                           NULL DEFAULT NULL,
    `birth_day`        datetime                                                      NULL DEFAULT NULL,
    `user_level`       int                                                           NULL DEFAULT NULL,
    `phone`            varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `role`             int                                                           NULL DEFAULT NULL,
    `status`           int                                                           NULL DEFAULT NULL,
    `image_path`       varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `create_time`      datetime                                                      NULL DEFAULT NULL,
    `modify_time`      datetime                                                      NULL DEFAULT NULL,
    `last_active_time` datetime                                                      NULL DEFAULT NULL,
    `deleted`          bit(1)                                                        NULL DEFAULT NULL,
    `wx_open_id`       varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user`
VALUES (1, 'd2d29da2-dcb3-4013-b874-727626236f47', 'student',
        'D1AGFL+Gx37t0NPG4d6biYP5Z31cNbwhK5w1lUeiHB2zagqbk8efYfSjYoh1Z/j1dkiRjHU+b0EpwzCh8IGsksJjzD65ci5LsnodQVf4Uj6D3pwoscXGqmkjjpzvSJbx42swwNTA+QoDU8YLo7JhtbUK2X0qCjFGpd+8eJ5BGvk=',
        '学生', 18, 1, '2019-09-01 16:00:00', 1, '19171171610', 1, 1,
        'https://www.mindskip.net:9008/image/ba607a75-83ba-4530-8e23-660b72dc4953/头像.jpg', '2019-09-07 18:55:02',
        '2020-02-04 08:26:54', NULL, b'0', NULL);
INSERT INTO `t_user`
VALUES (2, '52045f5f-a13f-4ccc-93dd-f7ee8270ad4c', 'admin',
        'D1AGFL+Gx37t0NPG4d6biYP5Z31cNbwhK5w1lUeiHB2zagqbk8efYfSjYoh1Z/j1dkiRjHU+b0EpwzCh8IGsksJjzD65ci5LsnodQVf4Uj6D3pwoscXGqmkjjpzvSJbx42swwNTA+QoDU8YLo7JhtbUK2X0qCjFGpd+8eJ5BGvk=',
        '管理员', 30, 1, '2019-09-07 18:56:07', NULL, NULL, 3, 1, NULL, '2019-09-07 18:56:21', NULL, NULL, b'0', NULL);
INSERT INTO `t_user`
VALUES (3, '3f607c35-bbc2-514e-a570-63e67690ce24', 'stu',
        '$2b$12$CrsYybGVO/VsaH3FSPKmk.GfcZY0X27DFrDvsyiBD8WS9gGZeQqPa', null, null, null, null, 7, null, null, null,
        null, null, null, null, null, null);

-- ----------------------------
-- Table structure for t_user_event_log
-- ----------------------------
DROP TABLE IF EXISTS `t_user_event_log`;
CREATE TABLE `t_user_event_log`
(
    `id`          int                                                           NOT NULL AUTO_INCREMENT,
    `user_id`     int                                                           NULL DEFAULT NULL,
    `user_name`   varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `real_name`   varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `content`     text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci         NULL,
    `create_time` datetime                                                      NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_user_event_log
-- ----------------------------

-- ----------------------------
-- Table structure for t_user_token
-- ----------------------------
DROP TABLE IF EXISTS `t_user_token`;
CREATE TABLE `t_user_token`
(
    `id`          int                                                           NOT NULL AUTO_INCREMENT,
    `token`       varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci  NULL DEFAULT NULL,
    `user_id`     int                                                           NULL DEFAULT NULL,
    `wx_open_id`  varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    `create_time` datetime                                                      NULL DEFAULT NULL,
    `end_time`    datetime                                                      NULL DEFAULT NULL,
    `user_name`   varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_general_ci
  ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_user_token
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;


-- t_exam_paper 表
INSERT INTO `t_exam_paper` (`name`, `subject_id`, `paper_type`, `grade_level`, `score`, `question_count`,
                            `suggest_time`, `limit_start_time`, `limit_end_time`, `frame_text_content_id`,
                            `create_user`, `create_time`, `deleted`, `task_exam_id`)
VALUES ('宪法基础知识测试01', 1, 1, 10, 32, 12, 60, '2023-01-01 08:00:00', '2023-01-02 08:00:00', 100, 1,
        '2023-01-01 08:00:00',
        0, 1);

# -- t_exam_paper_answer 表
# INSERT INTO `t_exam_paper_answer` (`exam_paper_id`, `paper_name`, `paper_type`, `subject_id`, `system_score`,
#                                    `user_score`, `paper_score`, `question_correct`, `question_count`, `do_time`,
#                                    `status`, `create_user`, `create_time`, `task_exam_id`)
# VALUES (1, 'Math Exam Answers', 1, 1, 90, 85, 100, 9, 10, 58, 1, 1, '2023-01-02 09:00:00', 1),
#        (2, 'Science Exam Answers', 2, 2, 140, 130, 150, 14, 15, 88, 1, 2, '2023-02-02 10:00:00', 2),
#        (3, 'English Exam Answers', 1, 3, 110, 105, 120, 11, 12, 73, 1, 2, '2023-03-02 11:00:00', 3);

# -- t_exam_paper_question_customer_answer 表
# INSERT INTO `t_exam_paper_question_customer_answer` (`question_id`, `exam_paper_id`, `exam_paper_answer_id`,
#                                                      `question_type`, `subject_id`, `customer_score`, `question_score`,
#                                                      `question_text_content_id`, `answer`, `text_content_id`,
#                                                      `do_right`, `create_user`, `create_time`, `item_order`)
# VALUES (1, 1, 1, 1, 1, 9, 10, 1, 'A', 1, 1, 1, '2023-01-02 09:01:00', 1),
#        (2, 1, 1, 2, 1, 9, 10, 2, 'C', 2, 1, 1, '2023-01-02 09:02:00', 2),
#        (3, 2, 2, 1, 2, 14, 15, 3, 'B', 3, 1, 1, '2023-02-02 10:01:00', 1),
#        (4, 2, 2, 2, 2, 14, 15, 4, 'D', 4, 1, 1, '2023-02-02 10:02:00', 2),
#        (5, 3, 3, 1, 3, 11, 12, 5, 'A', 5, 1, 1, '2023-03-02 11:01:00', 1),
#        (6, 3, 3, 2, 3, 11, 12, 6, 'C', 6, 1, 1, '2023-03-02 11:02:00', 2);

# -- t_message 表
# INSERT INTO `t_message` (`title`, `content`, `create_time`, `send_user_id`, `send_user_name`, `send_real_name`,
#                          `receive_user_count`, `read_count`)
# VALUES ('Important Notice', 'This is an important notice.', '2023-01-01 12:00:00', 1, 'admin', '管理员', 2, 0),
#        ('Exam Reminder', 'Don\'t forget about the upcoming exams.', '2023-02-01 13:00:00', 1, 'admin', '管理员', 2, 0),
#        ('Message from Teacher', 'You have a new message from your teacher.', '2023-03-01 14:00:00', 2, 'student',
#         '学生', 1, 0);

# -- t_message_user 表
# INSERT INTO `t_message_user` (`message_id`, `receive_user_id`, `receive_user_name`, `receive_real_name`, `readed`,
#                               `create_time`, `read_time`)
# VALUES (1, 1, 'admin', '管理员', 0, '2023-01-01 12:01:00', NULL),
#        (1, 2, 'student', '学生', 0, '2023-01-01 12:01:00', NULL),
#        (2, 1, 'admin', '管理员', 0, '2023-02-01 13:01:00', NULL),
#        (2, 2, 'student', '学生', 0, '2023-02-01 13:01:00', NULL),
#        (3, 2, 'student', '学生', 0, '2023-03-01 14:01:00', NULL);

-- t_subject 表
INSERT INTO `t_subject` (`id`, `name`, `level`, `level_name`, `item_order`, `deleted`)
VALUES (1, '宪法', 10, '本科一年级', 1, 0),
       (2, '民法', 10, '本科一年级', 2, 0),
       (3, '刑法', 10, '本科一年级', 3, 0),
       (4, '行政法', 10, '本科一年级', 4, 0),
       (5, '经济法', 10, '本科一年级', 5, 0),
       (6, '诉讼法', 10, '本科一年级', 6, 0),
       (7, '国际法', 10, '本科一年级', 7, 0);


# -- t_task_exam_customer_answer 表
# INSERT INTO `t_task_exam_customer_answer` (`task_exam_id`, `create_user`, `create_time`, `text_content_id`)
# VALUES (1, 2, '2023-01-01 10:01:00', 1),
#        (2, 2, '2023-02-01 10:01:00', 2),
#        (3, 1, '2023-03-01 10:01:00', 3);
#
# -- t_task_exam 表
# INSERT INTO `t_task_exam` (`title`, `grade_level`, `frame_text_content_id`, `create_user`, `create_time`, `deleted`,
#                            `create_user_name`)
# VALUES ('Final Exam', 10, 1, 1, '2023-01-01 10:00:00', 0, 'admin'),
#        ('Midterm Exam', 10, 2, 1, '2023-02-01 10:00:00', 0, 'admin'),
#        ('Unit Test', 10, 3, 2, '2023-03-01 10:00:00', 0, 'student');

-- t_question 表
# question_type: 1.单选题 2.多选题 3.判断题 4.填空题 5.简答题
INSERT INTO `t_question` (`id`, `question_type`, `subject_id`, `score`, `grade_level`, `difficult`, `correct`,
                          `info_text_content_id`, `create_user`, `status`, `create_time`, `deleted`)
VALUES (1, 1, 1, 3, 1, 3, 'A', 1, 1, 1, '2023-01-01 08:00:00', 0),
       (2, 1, 1, 3, 1, 3, 'C', 2, 1, 1, '2023-01-01 08:00:00', 0),
       (3, 1, 1, 3, 1, 3, 'B', 3, 1, 1, '2023-01-01 08:00:00', 0),
       (4, 2, 1, 5, 1, 4, '["A", "B", "C"]', 4, 1, 1, '2023-01-01 08:00:00', 0),
       (5, 2, 1, 5, 1, 4, '["A", "B", "C"]', 5, 1, 1, '2023-01-01 08:00:00', 0),
       (6, 2, 1, 5, 1, 4, '["A", "B", "C"]', 6, 1, 1, '2023-01-01 08:00:00', 0),
       (7, 3, 1, 2, 1, 4, 'A', 7, 1, 1, '2023-01-01 08:00:00', 0),
       (8, 3, 1, 2, 1, 4, 'A', 8, 1, 1, '2023-01-01 08:00:00', 0),
       (9, 3, 1, 2, 1, 4, 'A', 9, 1, 1, '2023-01-01 08:00:00', 0),
       (10, 4, 1, 2, 1, 3, '', 10, 1, 1, '2023-01-01 08:00:00', 0),
       (11, 4, 1, 2, 1, 3, '', 11, 1, 1, '2023-01-01 08:00:00', 0),
       (12, 4, 1, 2, 1, 3, '', 12, 1, 1, '2023-01-01 08:00:00', 0),
       (13, 5, 1, 2, 1, 10, '', 13, 1, 1, '2023-01-01 08:00:00', 0),
       (14, 5, 1, 2, 1, 10, '', 14, 1, 1, '2023-01-01 08:00:00', 0),
       (15, 5, 1, 2, 1, 10, '', 15, 1, 1, '2023-01-01 08:00:00', 0);

-- t_text_content 表
INSERT INTO `t_text_content` (`id`, `content`, `create_time`)
VALUES (1, '{
"titleContent": "我国宪法规定的国家制度是：",
"analyze": "宪法规定了我国的国家制度，正确理解我国宪法规定的国家制度对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "总统制",
"score": 0,
"itemUuid": "uuid5"
},
{
"prefix": "B",
"content": "议会制",
"score": 0,
"itemUuid": "uuid6"
},
{
"prefix": "C",
"content": "人民代表大会制",
"score": 3,
"itemUuid": "uuid7"
},
{
"prefix": "D",
"content": "部长制",
"score": 0,
"itemUuid": "uuid8"
}
],
"correct": "C"
}', '2023-01-01 08:00:00'),
       (2, '{
"titleContent": "宪法规定的我国的根本任务是：",
"analyze": "宪法规定了我国的根本任务，正确理解我国宪法规定的根本任务对于了解国家的发展方向具有重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "维护国家安全",
"score": 0,
"itemUuid": "uuid9"
},
{
"prefix": "B",
"content": "保障人民权利",
"score": 3,
"itemUuid": "uuid10"
},
{
"prefix": "C",
"content": "促进经济发展",
"score": 0,
"itemUuid": "uuid11"
},
{
"prefix": "D",
"content": "实现共产主义社会",
"score": 0,
"itemUuid": "uuid12"
}
],
"correct": "B"
}', '2023-01-01 08:00:00'),
       (3, '{
"titleContent": "宪法是国家的根本法，其地位在法律体系中属于：",
"analyze": "宪法在法律体系中具有特殊地位，它是国家的根本法，其他法律都应当与宪法相协调，不得与宪法相抵触。正确理解宪法在法律体系中的地位对于维护国家法制的正常运作至关重要。",
"questionItemObjects": [
{
"prefix": "A",
"content": "特殊法",
"score": 3,
"itemUuid": "uuid1"
},
{
"prefix": "B",
"content": "普通法",
"score": 0,
"itemUuid": "uuid2"
},
{
"prefix": "C",
"content": "行政法规",
"score": 0,
"itemUuid": "uuid3"
},
{
"prefix": "D",
"content": "地方法规",
"score": 0,
"itemUuid": "uuid4"
}
],
"correct": "A"
}', '2023-01-01 08:00:00'),
       (4, '{
"titleContent": "我国宪法规定的国家机关包括以下哪些？",
"analyze": "我国宪法规定了国家机关的组织形式，正确理解我国宪法规定的国家机关对于了解国家政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "国务院",
"score": 3,
"itemUuid": "uuid13"
},
{
"prefix": "B",
"content": "全国人民代表大会",
"score": 3,
"itemUuid": "uuid14"
},
{
"prefix": "C",
"content": "中央军委",
"score": 3,
"itemUuid": "uuid15"
},
{
"prefix": "D",
"content": "中央纪律检查委员会",
"score": 3,
"itemUuid": "uuid16"
}
],
"correct": ["A", "B", "C"]
}', '2023-01-01 08:00:00'),
       (5, '{
"titleContent": "我国宪法规定的国家制度是由以下哪些方面构成的？",
"analyze": "我国宪法规定了国家制度的构成要素，正确理解我国宪法规定的国家制度对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "国家性质",
"score": 3,
"itemUuid": "uuid17"
},
{
"prefix": "B",
"content": "国家机构",
"score": 3,
"itemUuid": "uuid18"
},
{
"prefix": "C",
"content": "国家权力机关",
"score": 3,
"itemUuid": "uuid19"
},
{
"prefix": "D",
"content": "国家领导人",
"score": 3,
"itemUuid": "uuid20"
}
],
"correct": ["A", "B", "C"]
}', '2023-01-01 08:00:00'),
       (6, '{
"titleContent": "我国宪法规定的国家机关的组织形式主要包括以下哪些？",
"analyze": "我国宪法规定了国家机关的组织形式，正确理解我国宪法规定的国家机关对于了解国家政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "人民法院",
"score": 3,
"itemUuid": "uuid21"
},
{
"prefix": "B",
"content": "人民检察院",
"score": 3,
"itemUuid": "uuid22"
},
{
"prefix": "C",
"content": "国务院",
"score": 3,
"itemUuid": "uuid23"
},
{
"prefix": "D",
"content": "全国人民代表大会",
"score": 3,
"itemUuid": "uuid24"
}
],
"correct": ["A", "B", "C"]
}', '2023-01-01 08:00:00'),
       (7, '{
"titleContent": "我国宪法规定的国家机关的组织形式主要包括人民法院、人民检察院、国务院。",
"analyze": "我国宪法对国家机关的组织形式进行了明确规定，正确理解我国宪法对国家机关的规定对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "正确",
"score": 3,
"itemUuid": "uuid25"
},
{
"prefix": "B",
"content": "错误",
"score": 3,
"itemUuid": "uuid26"
}
],
"correct": "A"
}', '2023-01-01 08:00:00'),
       (8, '{
"titleContent": "我国宪法规定的国家制度包括国家性质、国家机构、国家权力机关、国家领导人。",
"analyze": "我国宪法对国家制度进行了明确规定，正确理解我国宪法对国家制度的规定对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "正确",
"score": 3,
"itemUuid": "uuid27"
},
{
"prefix": "B",
"content": "错误",
"score": 3,
"itemUuid": "uuid28"
}
],
"correct": "A"
}', '2023-01-01 08:00:00'),
       (9, '{
"titleContent": "我国宪法规定的国家制度包括国家性质、国家机构、国家权力机关、国家领导人。",
"analyze": "我国宪法对国家制度进行了明确规定，正确理解我国宪法对国家制度的规定对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "A",
"content": "正确",
"score": 3,
"itemUuid": "uuid29"
},
{
"prefix": "B",
"content": "错误",
"score": 3,
"itemUuid": "uuid30"
}
],
"correct": "A"
}', '2023-01-01 08:00:00'),
       (10, '
{
"titleContent": "我国宪法规定的国家性质是______制。",
"analyze": "我国宪法对国家性质进行了明确规定，填写正确的国家性质对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "",
"content": "",
"score": 3,
"itemUuid": "uuid31"
}
],
"correct": "社会主义"
}', '2023-01-01 08:00:00'),
       (11, '{
"titleContent": "我国宪法规定的国家机构中，最高国家权力机关是______。",
"analyze": "我国宪法对国家机构进行了明确规定，填写正确的最高国家权力机关对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "",
"content": "",
"score": 3,
"itemUuid": "uuid36"
}
],
"correct": "国务院"
}', '2023-01-01 08:00:00'),
       (12, '{
"titleContent": "我国宪法规定的国家权力机关中，国家最高领导人是______。",
"analyze": "我国宪法对国家权力机关进行了明确规定，填写正确的国家最高领导人对于了解我国政治体制有着重要的意义。",
"questionItemObjects": [
{
"prefix": "",
"content": "",
"score": 3,
"itemUuid": "uuid37"
}
],
"correct": "国家主席"
}', '2023-01-01 08:00:00'),
       (13, '{
"titleContent": "解释我国宪法规定的国体和国家机构的基本原则。",
"analyze": "这是一道简答题，要求考生通过阐述我国宪法规定的国体和国家机构的基本原则，展示对我国政治体制的理解。",
"correct": "我国宪法规定的国体是社会主义制度，国家机构的基本原则包括人民代表大会制度、多党合作和政治协商制度以及民族区域自治制度。这些原则体现了我国的政治制度和国家组织结构，具有重要的法治意义。"
}', '2023-01-01 08:00:00'),
       (14, '{
"titleContent": "谈谈我国宪法对公民的基本权利和义务的规定。",
"analyze": "这是一道简答题，要求考生通过阐述我国宪法对公民的基本权利和义务的规定，展示对公民权利和责任的理解。",
"correct": "我国宪法规定了公民的基本权利，包括人身自由权、言论和出版自由、宗教信仰自由等。同时，宪法也规定了公民的基本义务，包括维护国家安全、遵守宪法和法律、保守国家秘密等。这些规定既保障了公民的权利，也明确了公民的责任。"
}', '2023-01-01 08:00:00'),
       (15, '{
"titleContent": "我国宪法规定了哪些国家机关和其职责？",
"analyze": "这是一道简答题，要求考生通过阐述我国宪法规定的国家机关及其职责，展示对我国政治体制和国家机构的理解。",
"correct": "我国宪法规定了多个国家机关，包括全国人民代表大会、国务院、全国人民检察院等，并明确了它们的职责。全国人民代表大会是最高国家权力机关，负责制定国家法律和决定重大事项。国务院是最高国家行政机关，负责执行法律和管理国家事务。全国人民检察院负责检察工作，保障法律的实施。"
}', '2023-01-01 08:00:00'),
       (100, '[
{"name":"单选题","ids":[1,2,3]},
{"name":"多选题","ids":[4,5,6]},
{"name":"判断题","ids":[8,9]},
{"name":"填空题","ids":[11,12]},
{"name":"简答题","ids":[14,15]}
]', '2023-01-01 08:00:00');

