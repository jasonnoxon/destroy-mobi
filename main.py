import glob
import os.path

# library_path = "/path/to/Calibre Library"
library_path = "/Users/jason/Documents/Calibre Library/"
count = 0


for filename in glob.iglob(library_path + '**/*', recursive=True):
    if filename.endswith("original_mobi"):
        os.remove(filename)
        print("Removed " + filename)

if count > 0:
    print("Removed " + str(count) + " files.")
else:
    print("No files removed.")
