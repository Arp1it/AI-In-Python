import os
import shutil

os.chdir("E:/m")
# print(os.getcwd())

for i in range(10):
    os.mkdir(str(i))
    os.chdir(str(i))
    for j in range(10):
        os.mkdir(str(j))
        os.chdir(str(j))
        for k in range(10):
            os.mkdir(str(k))
            os.chdir(str(k))
            for l in range(10):
                os.mkdir(str(l))

            os.chdir("..")

        os.chdir("..")

    os.chdir("..")
    
shutil.move("F:/reqquesttssmodule/1.png", "E:/m/8/2/7/3")