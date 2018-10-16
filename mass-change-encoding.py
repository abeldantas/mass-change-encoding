import os
import codecs
import sys


def list_files(directory, extension):
    r = []
    print(directory)
    print(extension)
    for root, dirs, files in os.walk(directory):
            for name in files:
                if name.endswith(extension):
                    r.append(os.path.join(root, name))
    return r


def change_encoding_for_file(path, source, dest):
    with codecs.open(path, 'r', encoding=source) as f:
        lines = f.read()
    with codecs.open(path, 'w', encoding=dest) as f:
        f.write(lines)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        for file in list_files(sys.argv[1], sys.argv[2]):
            change_encoding_for_file(file, sys.argv[3], sys.argv[4])
            print("Changed encoding for file " + file)
    else:
        print("Usage is 'mass-change-encoding <root-directory> <extension> <source-encoding> <destination-encoding>")
        print("Example: 'mass-change-encoding 'c:/Program Files/Adobe' .txt ansi utf-8'")
