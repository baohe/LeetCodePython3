# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        t1 = 1
        while (l1):
            sum1 += l1.val * t1
            l1 = l1.next
            t1 = t1 * 10
        sum2 = 0
        t2 = 1
        while (l2):
            sum2 += l2.val * t2
            l2 = l2.next
            t2 = t2 * 10
 
        sum = int(sum1) + int(sum2)

        node = ListNode(None)
        tmp_node = node
 
        if (sum == 0):
            return ListNode(0)
        while (sum):
            tmp_node.next = ListNode(sum % 10)
            tmp_node = tmp_node.next
            sum = sum // 10
        return node.next
