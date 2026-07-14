class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nxt = dummy
        pre = dummy
        count = 0
        
        # Count the total number of nodes
        while curr.next:
            curr = curr.next
            count += 1
            
        # Iterate through the list in groups of k
        while count >= k:
            curr = pre.next
            nxt = curr.next
            # Standard linked list reversal for k-1 links
            for i in range(1, k):
                curr.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = curr.next
            pre = curr
            count -= k
            
        return dummy.next
