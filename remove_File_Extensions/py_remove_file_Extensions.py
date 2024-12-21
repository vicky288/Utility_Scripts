import glob, os
folder = "."
for filename in glob.iglob(os.path.join(folder, '*.bat')):
    print (filename)
    if filename == ".\\run.bat":
        print ("skipped run.bat")
    else:
        os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.exe')):
    os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.dll')):
    os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.reg')):
    os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.ini')):
    os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.jar')):
    os.rename(filename, filename[:-4] + '')
for filename in glob.iglob(os.path.join(folder, '*.ps')):
    os.rename(filename, filename[:-3] + '')
for filename in glob.iglob(os.path.join(folder, '*.js')):
    os.rename(filename, filename[:-3] + '')