# class solution:
#     def replace(self,s):
#         result = s.replace(' ','20%')
#         return result
class solution:
    def replace(self, s: str) -> int:
        res = 0
        while '()' in s:
            s = s.replace('()','',1)
            res += 2
        return res
if __name__ == '__main__':
    S = solution()
    #s = input('请输入字符串')
    R = S.replace('()()()()((()))')
    print('替换后结果为%s'%R)

