def p(s):
    return s==s[::-1]
t=input()
if p(t):
    print("True")
else :
    print("False")