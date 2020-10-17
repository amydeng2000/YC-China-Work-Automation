class Solution:
    def swap(self, nums: List[int], a: int, b: int) -> None:
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocount += 1
            else:
                swap(nums, zerocount, i)

