from pathlib import Path
import os
import shutil

# print(Path.cwd())
# os.chdir('C:\\Windows\\System32')
# print(Path.cwd())
# os.chdir('C:/ThisFolderDoesNotExist')
# print(Path.home())
# print(Path('spam') / 'bacon' / 'eggs')
# print(Path('spam') / Path('bacon/eggs'))
# print(Path('spam') / Path('bacon', 'eggs'))
# print(Path('spam') / Path('bacon', 'eggs', 'ham'))
# Path(r'C:\Users\adrye\spam').mkdir(exist_ok=True)

# ## Getting the Parts of a Filepath

# p = Path('C:/Users/Al/spam.txt')
# print(p.anchor)
# print(p.parent)
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.drive)

## ORGANIZING FILES

h = Path.home()

shutil.copy(h / 'spam/file1.txt', h)

shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')

(h / 'spam2').mkdir()

shutil.move(h / 'spam/file1.txt', h / 'spam2')