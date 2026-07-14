import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a dummy node to simplify list construction
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # Add the head of each list to the heap
        for i, l in enumerate(lists):
            if l:
                # Include index 'i' to handle cases with identical values
                heapq.heappush(heap, (l.val, i, l))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If there's a next node, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
