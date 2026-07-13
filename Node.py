class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # 1. Create dummy node to handle head removal edge cases
    dummy = ListNode(0, head)
    first = dummy
    second = dummy
    
    # 2. Advance first pointer so there is an n-node gap
    for _ in range(n + 1):
        first = first.next
        
    # 3. Move first to the end, maintaining the gap
    while first:
        first = first.next
        second = second.next
        
    # 4. Skip the nth node from the end
    second.next = second.next.next
    
    return dummy.next
