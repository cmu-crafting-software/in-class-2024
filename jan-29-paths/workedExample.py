import glob
files = glob.glob('**/*.json', recursive=True)
print(files)
