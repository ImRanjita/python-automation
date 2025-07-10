from pathlib import Path

p1 = Path('Pathlib_exercise/hfg.txt')

# with open(p1, 'r') as file:
#     content = file.read()
#     print(content)

if not p1.exists():
    with open(p1, 'w') as file:
        file.write("This is a new file created because it did not exist.")
        print(f"File {p1} was created and written to.")

print(p1.name)
print(p1.stem)
print(p1.suffix)

dir_path = Path('Pathlib_exercise')
for item in dir_path.iterdir():
    print(item.name)