import os, sys, codecs
from os import write
os.chdir('//VBOXSVR/My_Passport')

with open('//VBOXSVR/My_Passport/cat.txt', "w") as text_file:
    for path, subdirs, files in os.walk(r'//VBOXSVR/My_Passport'):
        for filename in files:
            f = os.path.join(path, filename)        
            print(str(f))
            text_file.writelines(str(f))
