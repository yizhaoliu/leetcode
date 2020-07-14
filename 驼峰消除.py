class stack:
    def __init__(self):
        self.content = []
    def push(self,element):
        self.content.append(element)
    def pop(self):
        return self.content.pop()
    def size(self):
        return len(self.content)


def fun(str1):
    if not isinstance(str1,str):
        return str1
    if len(str1) < 3:
        return str1
    res = stack()
    for i in str1:
        if res.size() >= 2:
            p2 = res.pop()
            p1 = res.pop()
            if p1 == i and ((p1.islower() and p2.isupper()) or (p2.islower() and p1.isupper())and p1.lower() == p2):
                print("消除的是 %s%s%s"%(p1,p2,i))
            else:
                res.push(p1)
                res.push(p2)
                res.push(i)
        else:
            res.push(i)
    return "".join(res.content)

if __name__ == '__main__':
    res = fun("AaABCgCbD")
    print("消除驼峰后的是 %s" %(res))
