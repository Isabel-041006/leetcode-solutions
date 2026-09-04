# 2. Add Two Numbers

### Difficulty: Medium

## Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:


Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


 
Constraints:


	The number of nodes in each linked list is in the range [1, 100].
	0 <= Node.val <= 9
	It is guaranteed that the list represents a number that does not have leading zeros.

## Submission Details
- **Status**: Accepted
- **Runtime**: 12
- **Memory**: 12444000
- **Language**: python

## Code
```python
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
```
