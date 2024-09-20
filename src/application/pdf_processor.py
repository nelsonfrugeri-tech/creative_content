import os
import pdfplumber
import tiktoken
from translate.from_en_to_ptbr import FromEnToPtBR

class PDFProcessor:
    def __init__(self, pdf_path, output_dir='files/generate', max_tokens=8192, translate=False):
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        self.max_tokens = max_tokens
        self.text = ""
        self.segments = []
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
        self.translate = translate
        self.translator = FromEnToPtBR() if translate else None
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def read_pdf(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    self.text += extracted_text + "\n"

    def split_text(self):
        tokens = self.tokenizer.encode(self.text)
        total_tokens = len(tokens)
        start = 0
        while start < total_tokens:
            end = min(start + self.max_tokens, total_tokens)
            segment_tokens = tokens[start:end]
            segment_text = self.tokenizer.decode(segment_tokens)
            if self.translate:
                segment_text = self.translator.translate_text(segment_text)
            self.segments.append(segment_text)
            start = end

    def save_segments(self):
        for idx, segment in enumerate(self.segments, start=1):
            suffix = "_ptbr" if self.translate else ""
            file_path = os.path.join(self.output_dir, f"file_{idx}{suffix}.txt")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(segment)

    def process(self):
        self.read_pdf()
        self.split_text()
        self.save_segments()
