#冒泡排序
def bbsort(list1):
    n = len(list1)
    for i in range(1,n):
        ischange = True
        for j in range(n - i):
            if list1[j] > list1[j +1 ]:
                list1[j] , list1[j + 1] = list1[j + 1],list1[j]
                ischange = False
        if ischange:
            return list1
#快速排序
def QuickSort(alist, start, end):
    '''快速排序'''
    # 建立递归终止条件
    if start >= end:
        return
    low = start
    last = end
    mid_num = alist[start]
    while low < last:
        # 当low与last未重合，并且比基准元素要大，就将游标向左移动
        while low < last and alist[last] >= mid_num:
            last -= 1
        # 如果比基准元素小，就跳出循环，并且把其放在基准元素左边
        alist[low] = alist[last]
        # 当low与last未重合，并且比基准元素要小，就将游标向右移动
        while low < last and alist[low] < mid_num:
            low += 1
        # 如果比基准元素大，就跳出循环，并且把其放在基准元素右边
        alist[last] = alist[low]
    # 当low与last相等，就是mid_num的排序位置
    alist[low] = mid_num
    # 然后对排序好的元素左右两边的序列进行递归
    QuickSort(alist, start, low - 1)  # 对左边的序列进行递归
    QuickSort(alist, low + 1, end)  # 对右边的序列进行递归


if __name__ == '__main__':
    alist = [30, 40, 60, 10, 20, 50]
    print(alist)
    QuickSort(alist, 0, len(alist) - 1)
    print(alist)