class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode() #构造哑节点
        carry = 0 #进位

        while l1 or l2 or carry: #链表1还没有遍历完，还有位上的数字需要相加
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 #l1 和 l2 有可能长度不一样，其中一个提前走完了变成了空。如果指针还在，就取它的值；如果指针已经走到头变成了空，就把它当成 0 来加

            total = v1 + v2 + carry
            carry,digit = divmod(total,10) #divmod()会同时计算除法和取余数

            curr.next = ListNode(digit)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next