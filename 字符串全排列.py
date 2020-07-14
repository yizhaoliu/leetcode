def Permutation( ss):
    if len(ss) <= 1:
        return ss
    charlist = list(ss)
    str_list = []
    charlist.sort()
    for i in range(len(charlist)):
        if i > 0 and charlist[i] == charlist[i - 1]:
            continue
        str_sort = Permutation(charlist[0:i] + charlist[i + 1:])
        for j in str_sort:
            str_list.append(charlist[i] + j)
    return str_list

if __name__ == '__main__':
    ss = 'abbc'
    res = Permutation(ss)
    print(res)