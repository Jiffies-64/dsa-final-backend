import uuid


class UUIDGenerator:
    @staticmethod
    def generate_uuid_from_string(input_string):
        # 使用SHA-1散列生成UUID
        uuid_obj = uuid.uuid5(uuid.NAMESPACE_DNS, str(input_string))
        return str(uuid_obj)


if __name__ == '__main__':
    # 示例用法：
    input_str = "example_string"
    generated_uuid = UUIDGenerator.generate_uuid_from_string(input_str)
    print("Generated UUID:", generated_uuid)
