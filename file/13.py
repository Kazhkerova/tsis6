import os
def s(p):
    if os.path.exists(p) and os.access(p, os.W_OK):
        os.remove(p)
        print("File delete")
    else:
        print("File not found.")

n="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file/14.py"
s(n)