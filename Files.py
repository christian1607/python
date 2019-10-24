from pathlib import Path


path = Path()
print(path.absolute())

for file in path.glob("*.*"):
    print(file)
    #print(file.owner())

path2 = Path("backup2")

print(path2.exists())
path2.mkdir()
print(path2.exists())








