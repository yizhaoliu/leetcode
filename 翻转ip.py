# @coding   : ctf-8
# @Author   : liuyizhao
# @Time     : 2019/12/11 12:30
# @File     : 字符串翻转.py
# @Software : PyCharm
class Reverse:
    def fun(self,str):
        i = len(str)
        s1 = ''
        for j in range(len(str)-1,-1,-1):
            if str[j] =='.' or str[j] =='/':
                str1 = str[j+1:i]
                s1 = s1 + str1
                s1 = s1 + str[j]
                i = j
        s1 = s1 + str[0:i]
        return s1
if __name__ == '__main__':
    str = 'www.toutiao.com/p/index.html'
    R = Reverse()
    result = R.fun(str)
    print(result,end=' ')