import os
from os import listdir, getcwd

#path = "C:\\Users\\bhpradha\\Desktop\\scripts\\deleteFilesFromAList"
path = getcwd()
os.chdir(path)
flist = open('i_list_delete_files.txt')
ctr =0
for f in flist:
    fname = f.rstrip() # or depending on situation: f.rstrip('\n')
    fname = fname.lower()
    # or, if you get rid of os.chdir(path) above,
    # fname = os.path.join(path, f.rstrip())
    if os.path.isfile(fname): # this makes the code more robust
        ctr = ctr + 1
        os.remove(fname)
# also, don't forget to close the text file:
flist.close()
print (ctr)