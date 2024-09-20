import os
import tiktoken 
from llm.openai_client import OpenAIClient
from translate.from_en_to_ptbr import FromEnToPtBR

class ScriptGenerator:
    def __init__(self, input_dir: str, output_script: str, max_tokens: int = 16384):
        self.input_dir = input_dir
        self.output_script = output_script
        self.max_tokens = max_tokens
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
        self.openai_client = OpenAIClient()
        self.accumulated_text = ""

    def count_tokens(self, text: str) -> int:
        """Conta o número de tokens do texto."""
        return len(self.tokenizer.encode(text))

    def accumulate_text(self):
        """Acumula o texto dos arquivos .txt até atingir o limite de tokens permitido."""
        total_tokens = 0

        for file_name in sorted(os.listdir(self.input_dir)):
            file_path = os.path.join(self.input_dir, file_name)

            if file_name.endswith(".txt") and os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                content_tokens = self.count_tokens(content)

                # Verifica se a adição desse conteúdo ultrapassaria o limite de tokens
                if total_tokens + content_tokens > self.max_tokens:
                    break

                self.accumulated_text += content
                total_tokens += content_tokens

        print(f"Texto acumulado contém {total_tokens} tokens.")

    def generate_script(self):
        """Gera o script usando a API da OpenAI."""
        # Define o prompt para a criação do script de aula
        prompt = (
            "Você é especialista em data driven e liderança técnica e negócios empresariais."
            "Seu objetivo é ensinar as pessoas sobre o tema de métricas de design."
            "Sua abordagem é simples e ao mesmo tempo intelectual, você escreve de maneira clara e objetiva."
            "Com base no seguinte texto, crie um script natural e fluido para uma aula ou treinamento."
            "O script deve ser escrito com o objetivo de ser lido em voz alta para uma audiência."
            "Não use caracteres especiais, use apenas texto simples."
            "Use gírias e palavras próprias do português do Brasil, mantendo os fundamentos e a ideia original."
            "Não traduza os termos técnicos e os jargões do mundo empresarial e de tecnologia, mantenha-os sempre em inglês."            
        )

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": self.accumulated_text},
        ]

        response = self.openai_client.generate_text(
            messages=messages,
            model="chatgpt-4o-latest",
        )

        # Salva o script gerado em um arquivo
        with open(self.output_script, "w", encoding="utf-8") as file:
            file.write(response)

        print(f"Script gerado e salvo em {self.output_script}")

if __name__ == "__main__":
    # Diretório ptbr onde estão os arquivos .txt
    input_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "generative",
        "data_driven__metric_design",
        "ptbr"
    )

    # Caminho de saída para o script gerado
    output_script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "files",
        "generative",
        "data_driven__metric_design",
        "ptbr",
        "script_metric_design.txt"
    )

    # Criação do gerador de script
    script_generator = ScriptGenerator(input_dir=input_dir, output_script=output_script)
    
    # Acumula o texto até atingir o limite de tokens
    script_generator.accumulate_text()
    
    # Gera o script usando a API da OpenAI
    script_generator.generate_script()
