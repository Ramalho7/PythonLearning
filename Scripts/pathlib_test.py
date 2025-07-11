from pathlib import Path
import os
import shutil
print(Path.cwd())
os.chdir('C:\\Windows\\System32')
print(Path.cwd())
# os.chdir('C:/ThisFolderDoesNotExist')
print(Path.home())
print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))
print(Path('spam') / Path('bacon', 'eggs', 'ham'))
# Path(r'C:\Users\adrye\spam').mkdir()

## Getting the Parts of a Filepath

p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

## ORGANIZING FILES



