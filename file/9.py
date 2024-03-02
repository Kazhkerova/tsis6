def count(f):
    with open(f,'r') as file:
        l=sum(1 for line in file)
        print(l)

name="/Users/asus2/OneDrive/Рабочий стол/pp2/tsis6/file/6.py"
count(name)