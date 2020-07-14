def sortfun(str,n):
    dic = {}
    res = []
    for i in str:
        dic[i] = dic.get(i,0) + 1
    dr = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for i in dr:
        print(i)
    for i in range(n):
        print(i)
        res.append(dr[i][0])
    return res

if __name__ == '__main__':
    str= "asdfghygfttfdft"
    print(sortfun(str,3))
