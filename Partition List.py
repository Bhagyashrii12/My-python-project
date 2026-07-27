class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)

        smallTail = small
        largeTail = large

        while head:
            if head.val < x:
                smallTail.next = head
                smallTail = smallTail.next
            else:
                largeTail.next = head
                largeTail = largeTail.next

            head = head.next

        largeTail.next = None
        smallTail.next = large.next

        return small.next
