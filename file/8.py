import os
def an(p):
    if os.path.exists(p):
        print(p)
        print(os.path.dirname(p))
        print(os.path.basename(p))
    else:
        print("Not exist")

name="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file"
an(name)