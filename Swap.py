class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    
    while prev.next and prev.next.next:
        # Identify nodes to swap
        first = prev.next
        second = prev.next.next
        
        # Swapping pointers
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move prev forward for the next pair
        prev = first
        
    return dummy.next
