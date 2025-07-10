from pathlib import Path
root_dir = Path('Pathlib_exercise')
Filepath = root_dir.iterdir()
# print(list(Filepath))

for path in Filepath:
    new_filename = "new-"+ path.stem + path.suffix
    new_filePath = path.with_name(new_filename)
    print(new_filePath)
    path.rename(new_filePath)