from flask import jsonify


class Resp:
    def __init__(self, code, message, resp):
        self.code = code
        self.message = message
        self.response = resp

    def data(self):
        def to_dict_recursive(obj):
            if obj is not None and hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
                return obj.to_dict()
            elif isinstance(obj, (list, tuple)):
                return [to_dict_recursive(item) for item in obj]
            elif isinstance(obj, dict):
                return {key: to_dict_recursive(value) for key, value in obj.items()}
            else:
                return obj

        response_data = to_dict_recursive(self.response)

        return jsonify({
            "code": self.code,
            "message": self.message,
            "response": response_data
        })
