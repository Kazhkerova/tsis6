def l_l(p,l):
    with open (p,'w') as file:
        for i in l:
            file.write(str(i)+'\n')

li=["i1","i2","i3"]
path="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file/p.txt"
l_l(path,li)