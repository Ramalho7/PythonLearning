from pathlib import Path
import pypdf

with open(Path(__file__).parent / 'dictionary.txt', encoding='utf-8') as dictionary:
    dictionary_list = [line.strip() for line in dictionary]

reader = pypdf.PdfReader('encrypted.pdf')
for password in dictionary_list:
    if reader.decrypt(password):
        print(f'Password corret: {password}')
else:
    print(f'Password not found')

