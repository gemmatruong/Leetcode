import heapq

class KthLargest:
    # Use sort(reverse=True) to sort every time adding a new value. 
    # def __init__(self, k: int, nums: List[int]):
    #     self._index = k
    #     self._record = sorted(nums, reverse = True)

    # def add(self, val: int) -> int:
    #     self._record.append(val)
    #     self._record.sort(reverse=True)
    #     return self._record[self._index-1]
    
    # Use minheap
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Turn the list into a min-heap

        # Keep only the k largest elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)

        # If the heap grows larger than k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root of the heap is the kth largest element
        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def main():
    print("Test Case 1:")
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # → 4
    print(kth.add(5))   # → 5
    print(kth.add(10))  # → 5
    print(kth.add(9))   # → 8
    print(kth.add(4))   # → 8

    print("\nTest Case 2:")
    kth = KthLargest(1, [])
    print(kth.add(-3))  # → -3
    print(kth.add(-2))  # → -2
    print(kth.add(-4))  # → -2
    print(kth.add(0))   # → 0
    print(kth.add(4))   # → 4

    print("\nTest Case 3:")
    kth = KthLargest(2, [10, 7, 11])
    print(kth.add(5))   # → 10
    print(kth.add(13))  # → 11

    print("\nTest Case 4:")
    kth = KthLargest(3, [1, 2])
    print(kth.add(3))   # → 1
    print(kth.add(4))   # → 2

    print("\nTest Case 5:")
    kth = KthLargest(4, [5, -1, 10, 2, 7])
    print(kth.add(3))   # → 3
    print(kth.add(8))   # → 5

    print("\nTest Case 6:")
    kth = KthLargest(2, [100, 50, 200])
    print(kth.add(150)) # → 150
    print(kth.add(300)) # → 200

    print("\nTest Case 7:")
    kth = KthLargest(3, [1, 1, 1])
    print(kth.add(1))   # → 1
    print(kth.add(2))   # → 1

    print("\nTest Case 8:")
    kth = KthLargest(2, [9])
    print(kth.add(10))  # → 9
    print(kth.add(8))   # → 9
    print(kth.add(11))  # → 10

    print("\nTest Case 9:")
    kth = KthLargest(3, [])
    print(kth.add(5))   # → 5
    print(kth.add(10))  # → 5
    print(kth.add(9))   # → 5
    print(kth.add(4))   # → 5
    print(kth.add(15))  # → 9

    print("\nTest Case 10:")
    kth = KthLargest(5, [3, 2, 4, 1])
    print(kth.add(5))   # → 1
    print(kth.add(6))   # → 2
    print(kth.add(0))   # → 2
    print(kth.add(10))  # → 3


if __name__ == "__main__":
    main()