#翻转链表
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def fun4(pHead):
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        lpoint = pHead
        mpoint = lpoint.next
        rpoint = mpoint.next
        lpoint.next = None
        while rpoint != None:
            mpoint.next = lpoint
            lpoint = mpoint
            mpoint = rpoint
            rpoint = rpoint.next
        mpoint.next = lpoint
        return mpoint
    def fun5(head,k):
        dummy = Node(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 目前tmp所在k+1位置,说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp
        return dummy.next


# 测试用例
if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(3)
    l1.next.next.next = Node(4)
    l1.next.next.next.next = Node(5)
    #l = Solution.fun4(l1)
    #print(l.val, l.next.val, l.next.next.val, l.next.next.next.val,l.next.next.next.next.val)
    l2 = Solution.fun5(l1,2)
    while l2:
        print(l2.val)
        l2 = l2.next