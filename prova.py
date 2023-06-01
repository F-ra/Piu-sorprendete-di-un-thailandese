
print('Questo è un file python')

a=2
b=3

print('a =',a)
print('b =',b)
print('a+b =',a+b)

xc = input("Bel Culo: ")

bum = input("nice ass: ")

print("", )

def stringconcat(str1, str2):
    gulag = []
    a = 0
    for v in range(len(str1) + len(str2)):
        gulag[a] = str1[a]
        a = a + 1
        if a == (len(str1) - 1):
            a = 0
            break
    print(gulag)

stringconcat(xc, bum)