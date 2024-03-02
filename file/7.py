import os
def s(d):
    print(os.path.exists(d))#existence
    print(os.access(d,os.R_OK))#read
    print(os.access(d,os.W_OK))#write
    print(os.access(d,os.X_OK))#executability
name="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file"
s(name)