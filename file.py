with open('referat.txt', 'r', encoding='utf-8') as f, open('referat2.txt', 'w', encoding='utf-8') as out:
    le = 0
    words = 0
    for lin in f:
        l = lin.rstrip()
        words += len(l.split())
        le += len(l)
        new = lin.replace('.', '!')
        n = out.write(new)
    print(le)
    print(words)  