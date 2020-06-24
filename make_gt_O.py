import glob
import os

path = '/home/bhanu/datasets/tesseractMICR/datasets/e13b/'

c = 0
for files in glob.glob(path+"*.txt"):
    c = c + 1
    img_name = files.rsplit(".")[0]+".png"
    txt_file = open(files,"r")
    txt = txt_file.readline()
    txt_file.close()
    f = open("gt_txt.txt","a")
    f.write(img_name+"\t"+txt+"\n")
    os.remove(files)
print(c)
