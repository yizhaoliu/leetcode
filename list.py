def pp(str):
    l=[]
    for i in str:
        l.append(i)
    p = l.pop(0)
    return p
if __name__ == '__main__':
    p = pp('asdfg')
    print(p)
    dp = [[0 for j in range(4)] for i in range(2)]
    print(dp)
    s = "hello world"
    ns = s.split(' ')
    res = []
    for i in ns:
        res.append(i.capitalize())
    nres = " ".join(res)
    print(nres)