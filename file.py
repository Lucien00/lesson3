with open('referat.txt', 'r', encoding='utf-8') as f:
    fil = f.read()
    print(len(fil))
    words = fil.split()
    print(len(words))
    
with open('referat2.txt', 'w', encoding='utf-8') as f:
    fil = f.write(fil.replace('.', '!'))