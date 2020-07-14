def EntryNodeOfLoop(self, pHead):
    # write code here
    fp = pHead
    sp = pHead
    while fp != None and fp.next != None:
        fp = fp.next.next
        sp = sp.next
        if fp == sp:
            break
    if fp == None or fp.next == None:
        return None
    fp = pHead
    while sp != fp:
        fp = fp.next
        sp = sp.next
    return fp