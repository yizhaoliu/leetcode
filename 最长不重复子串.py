def lengthOfLongestSubstring(s):
    # 存储历史循环中最长的子串长度
    max_len = 0
    # 判断传入的字符串是否为空
    if s is None or len(s) == 0:
        return max_len
    # 定义一个字典，存储不重复的字符和字符所在的下标
    str_dict = {}
    one_max = 0
    # 记录最近重复字符所在的位置+1
    start = 0
    for i in range(len(s)):
        # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
        if s[i] in str_dict and str_dict[s[i]] >= start:
            # 记录当前字符的值+1
            start = str_dict[s[i]] + 1
            #print(str(start)+'*')
        # 在此次循环中，最大的不重复子串的长度
        one_max = i - start + 1
        # 把当前位置覆盖字典中的位置
        str_dict[s[i]] = i
        # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
        max_len = max(max_len, one_max)
    return max_len

def fun(s):
    tmp = ''
    r = 0
    for v in s:
        if v not in tmp:
            tmp += v
        else:
            n = tmp.index(v)
            tmp = tmp[n + 1:] + v
            print(tmp)
        r = max(len(tmp), r)
    return r
print(lengthOfLongestSubstring('pwawssffasdf'))
print(fun('pwawssffasdf'))