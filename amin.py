import os
from deep_translator import GoogleTranslator

os.chdir(r"C:\Users\aliha\OneDrive\Documents\python\data")

with open('source.txt', 'r') as source_fiel:
    content = source_fiel.read()
    translator = GoogleTranslator(source='en', target='ar')
    translation = translator.translate(content)


    with open('trans_ar.txt', 'w', encoding="utf-8") as target_fiel:
        target_fiel.write(translation)

