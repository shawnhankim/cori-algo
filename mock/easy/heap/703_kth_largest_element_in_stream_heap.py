"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.

"""

from heapq import heappush, heappop, heapify, heappushpop

# Runtime: 92 ms
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapify(self.nums)
        
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k: heappush(self.nums, val)
        else                      : heappushpop(self.nums, val)
        return self.nums[0]


# Runtime: 1716 ms    
class KthLargest2:
    def __init__(self, k, nums):
        self.nums, self.k = sorted(nums), k
        
    def add(self, val):
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[len(self.nums)-self.k]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

