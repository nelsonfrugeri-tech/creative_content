import os
from translate.from_en_to_ptbr import FromEnToPtBR


import os
from translate.from_en_to_ptbr import FromEnToPtBR

def translate_content(input_dir: str) -> None:
    ptbr_dir = os.path.join(input_dir, "ptbr")
    os.makedirs(ptbr_dir, exist_ok=True)

    translator = FromEnToPtBR()

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)

        if file_name.endswith(".txt") and os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            print(f"Traduzindo o arquivo {file_name}...")

            translated_content = translator.translate_text(content)
            
            translated_file_path = os.path.join(ptbr_dir, file_name)
            with open(translated_file_path, 'w', encoding='utf-8') as translated_file:
                translated_file.write(translated_content)

            print(f"Tradução do arquivo {file_name} salva em {translated_file_path}")




if __name__ == "__main__":
    translate_content(
        input_dir=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "files",
            "generative",
            "data_driven__metric_design",
        )
    )
