def twoSum(nums,target):
    # 用len()方法取得nums列表长度
    n = len(nums)
    # 创建一个空字典
    d = {}
    for x in range(n):
        a = target - nums[x]
        # 字典d中存在nums[x]时
        if nums[x] in d:
            return d[nums[x]], x
        # 否则往字典增加键/值对
        else:
            d[a] = x
if __name__ == '__main__':
    res = twoSum([1,3,5,7,4],7)
    print(res)