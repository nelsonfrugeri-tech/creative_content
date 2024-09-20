from llm.openai_client import OpenAIClient

class FromEnToPtBR:
    def __init__(self):
        self.openai_client = OpenAIClient()
        self.system_prompt = "You are a professional translator. Translate the following English text to Brazilian Portuguese (pt-BR) accurately and preserve the original meaning."

    def translate_text(self, text):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text}
        ]
        return self.openai_client.generate_text(messages=messages)
