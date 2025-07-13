import pypdf

writer = pypdf.PdfWriter()
writer.append('Recursion_Chapter1.pdf')
writer.encrypt('aaaaaahhhhh', algorithm='AES-256')
with open('encrypted.pdf', 'wb') as file:
    writer.write(file)
    
reader = pypdf.PdfReader('encrypted.pdf')
print(reader.is_encrypted)
reader.decrypt('an incorrect password').name
reader.decrypt('aaaaaahhhhh').name
writer.append(reader)
with open('decrypted.pdf', 'wb') as file:
    writer.write(file)