# from collections import Counter
# def find(xlist):
#     result = Counter(xlist)
#     dr = sorted(result.items(), key=lambda x: x[1], reverse=True)
#     print(result)
#     dictnew = dict(dr)
#     print(dictnew)
#     nlist = list(dictnew.values())
#     print(nlist)
#     c = 1
#     for i in range(len(nlist)-1):
#         if nlist[i] == nlist[i + 1]:
#             c = c + 1
#         else:
#             break
#     if c == 1:
#         return list(dictnew.keys())[list(dictnew.values()).index(nlist[0])]
#     else:
#         l1 = dr[:c]
#         data = dict(l1)
#         print(data)
#         L = sorted(data.keys())
#         return L[0]
#
# if __name__ == '__main__':
#     x = input()
#     xlist = x.split(",")
#     p=find(xlist)
#     print(p)
#
#

for i in range(1,10):
     for j in  range(1,i+1):
        print("%d*%d=%2d"%(j,i,j*i),end=' ')
     print("")



class Solution:
    def Treeh(self,pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeh(pRoot.left)
        rh = self.Treeh(pRoot.right)
        return max(lh,rh) + 1
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return abs(self.Treeh(pRoot.left) - self.Treeh(pRoot.right)) <= 1