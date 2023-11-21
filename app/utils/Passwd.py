import bcrypt


class PasswordHasher:
    @staticmethod
    def hash_password(password):
        # 生成哈希值并返回
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')  # 将 bytes 转换为字符串存储

    @staticmethod
    def check_password(password, hashed_password):
        # 验证密码是否匹配
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


if __name__ == '__main__':
    # 示例用法：
    # 哈希密码
    hashed_password = PasswordHasher.hash_password("user_password")
    print("Hashed Password:", hashed_password)

    # 验证密码
    password_to_check = "user_password"
    if PasswordHasher.check_password(password_to_check, hashed_password):
        print("Password is correct!")
    else:
        print("Password is incorrect!")
