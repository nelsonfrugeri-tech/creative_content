import os
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_audio(self, text, output_path):
        response = self.client.Audio.create(
            model="tts-1",
            input=text
        )
        audio_content = response['audio_content']
        with open(output_path, 'wb') as audio_file:
            audio_file.write(audio_content)
        return output_path

    def generate_text(self, messages, model="gpt-4o", temperature=0):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content
