import glob
import os
from PIL import Image

for i in glob.glob('images/*.jfif', recursive=True):
    print(i)
    img = Image.open(i)
    path1 = os.path.split(i)[0]
    path2 = os.path.split(i)[1].replace("jfif","png")
    new_path = os.path.join(path1,path2)
    img.save(new_path)