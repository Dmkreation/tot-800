import sys
import os
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-fr-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-fr-en")


def format_text(text):
    return re.sub('[^a-zA-Z ]+', '', text)


def translate_text_file(txt_path, output_file):
    txt_file = open(txt_path, 'rb')
    text = txt_file.read()
    txt_file.close()

    # Décodez le contenu en utilisant l'encodage approprié
    text = text.decode("utf-8")

    formated_text = tuple(map(format_text, text.split()))
    input_ids = tokenizer.encode(formated_text, return_tensors="pt")
    translated = model.generate(input_ids)
    output_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    output_file = open(output_file, "w")
    output_file.write(output_text)
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
