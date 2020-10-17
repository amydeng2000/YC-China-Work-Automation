import glob2
from os import rename
import pathlib

files = []
i = 0
num = ""
# for file in glob2.glob("./emails/*.png"):
#     i += 1
#     if i < 10:
#         num = "00{0}-".format(i)
#     elif i < 100:
#         num = "0{0}-".format(i)
#     else:
#         num = "{0}-".format(i)
#     rename(file, num+file[9:])




# currentDirectory = pathlib.Path('./emails')
# for currentFile in currentDirectory.iterdir():
#     print(currentFile)

for file in glob2.glob("./emails/*.png"):
    print(file[9:37])

