import os
def file(p):
    print([n for n in os.listdir(p) if os.path.isfile(os.path.join(p,n))])#directory name
    print([s for s in os.listdir(p) if os.path.isfile(os.path.join(p,s))])#file name
    print(os.listdir(p))

name="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file"
file(name)