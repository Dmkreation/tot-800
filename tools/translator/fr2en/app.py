import sys
import os
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")


def format_text(text):
    return re.sub('[^a-zA-Z ]+', '', text)


def translate_text_file(txt_path, output_path):
    print(f"Start translation of {txt_path}")
    txt_file = open(txt_path, 'rb')
    text = txt_file.read()
    txt_file.close()

    text = text.decode("utf-8")
    max_length = 512
    text_segments = [text[i:i+max_length]
                     for i in range(0, len(text), max_length)]
    total_segment = len(text_segments)
    count = 1
    with open(output_path, "w+") as output_file:
        for segment in text_segments:
            print(f"{count}/{total_segment} Segment(s)")
            input_ids = tokenizer.encode(segment, return_tensors="pt")
            translated = model.generate(input_ids)
            decoded = tokenizer.decode(translated[0], skip_special_tokens=True)
            output_file.write(f" {decoded}")
            count += 1
        output_file.close()

    print(
        f"Traduction terminée. Le texte a été sauvegardé dans {output_file}.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Veuillez spécifier le chemin vers le fichier TXT en argument.")
    else:
        txt_path = sys.argv[1]
        output_file = f"{os.environ['FR2EN_TRANSLATOR_PATH']}/exchange/{os.path.basename(txt_path).replace('.txt', '-en.txt')}"
        translate_text_file(txt_path, output_file)
