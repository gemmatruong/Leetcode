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
    """
    Run 10 distinct test cases for the KthLargest class.
    Each test case uses assertions to verify correctness.
    """
    # Test case 1
    obj1 = KthLargest(3, [4, 5, 8, 2])
    assert obj1.add(3) == 4, "TC1 failed: expected 4"

    # Test case 2
    obj2 = KthLargest(1, [-1, 2, 3])
    assert obj2.add(4) == 4, "TC2 failed: expected 4"

    # Test case 3 – empty initial list
    obj3 = KthLargest(2, [])
    assert obj3.add(5) == 5, "TC3 failed: expected 5"
    assert obj3.add(10) == 5, "TC3 failed: expected 5 after adding 10"

    # Test case 4 – adding a larger element
    obj4 = KthLargest(3, [1, 2, 3, 4, 5])
    assert obj4.add(6) == 4, "TC4 failed: expected 4"

    # Test case 5 – k larger than initial size
    obj5 = KthLargest(4, [10, 9, 8])
    assert obj5.add(7) == 7, "TC5 failed: expected 7"

    # Test case 6 – duplicate removal after adding
    obj6 = KthLargest(2, [100, 200])
    assert obj6.add(150) == 150, "TC6 failed: expected 150"

    # Test case 7 – negative numbers, k larger than current heap
    obj7 = KthLargest(5, [-5, -10, -3])
    assert obj7.add(-1) == -10, "TC7 failed: expected -10"

    # Test case 8 – all zeros
    obj8 = KthLargest(3, [0, 0, 0])
    assert obj8.add(0) == 0, "TC8 failed: expected 0"

    # Test case 9 – adding a very small number
    obj9 = KthLargest(2, [1, 2])
    assert obj9.add(-100) == 1, "TC9 failed: expected 1"

    # Test case 10 – adding a larger number
    obj10 = KthLargest(3, [5, 4, 3])
    assert obj10.add(6) == 4, "TC10 failed: expected 4"

    # Additional sanity check – large numbers
    large_obj = KthLargest(3, [10**9, 10**9 - 1, 10**9 - 2])
    assert large_obj.add(10**9 + 5) == 10**9 - 1, "Large TC failed: expected 10**9 - 1"

    print("All 10 test cases passed successfully!")


if __name__ == "__main__":
    main()