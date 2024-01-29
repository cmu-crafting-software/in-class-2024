import glob
files = glob.glob('**/*.csv', recursive=True)
print(files)