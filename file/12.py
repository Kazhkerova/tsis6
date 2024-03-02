def copy(old,new):
    with open(old,'r') as file, open (new,'w') as n:
        n.write(file.read())

old="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file/A.txt"
new="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file/B.txt"
copy(old,new)
