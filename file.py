def file():
    # 打开文件
    #p = r"D:\test\1test.txt"
    f = open(r'D:\test\1test.txt', encoding='UTF-8')
    # 读取文件一行
    content = f.readlines()
    for i in content:
        # 以空格区分返回集合
        list = i.split(' ')
        # print(list )
        # print('******************')
        for t in list:
            # 截取以.com结尾的字符串
            if '.com' in t:
                print(t)
    f.close()
if __name__ == '__main__':
    file()