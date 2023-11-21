import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig


class LawLLM:
    _instance = None  # 单例模式的实例
    model = None
    tokenizer = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LawLLM, cls).__new__(cls)
            cls._instance.init_model()
        return cls._instance

    def init_model(self):
        print("Initializing model...")
        # model_path = "ShengbinYue/DISC-LawLLM"
        # offload_folder = r"D:\NJU\2023-dsa-Final\final\dsa-final-backend\offload"
        # self.model = AutoModelForCausalLM.from_pretrained(
        #     model_path, torch_dtype=torch.float16, device_map="auto", trust_remote_code=True,
        #     offload_folder=offload_folder
        # )
        # self.model.generation_config = GenerationConfig.from_pretrained(model_path)
        # self.tokenizer = AutoTokenizer.from_pretrained(
        #     model_path, use_fast=False, trust_remote_code=True
        # )
        print("Model is ready!")

    def get_model_and_tokenizer(self):
        if self.model is None or self.tokenizer is None:
            print("Model is None!!! Initializing...")
        return self.model, self.tokenizer

    def chat(self, messages, stream=True):
        position = 0
        response = 'None'
        try:
            for response in self.model.chat(self.tokenizer, messages, stream=stream):
                print(response[position:], end="", flush=True)
                position = len(response)
                if torch.backends.mps.is_available():
                    torch.mps.empty_cache()
        except KeyboardInterrupt:
            pass
        finally:
            return response

    # def chat(self, prompt, stream=True):
    #     self.messages.append({"role": "user", "content": prompt})
    #     return self.model.chat(self.tokenizer, self.messages, stream=stream)


if __name__ == "__main__":
    chatbot = LawLLM()
    resp = chatbot.chat({"role": "user", "content": "你好"})
    print(resp)
