def fun(str):
    result = []
    for i in range(len(str)):
        for j in range(len(str) - i):
            result.append(str[j:j + i + 1])
    return result
if __name__ == '__main__':
    print(fun('abc'))