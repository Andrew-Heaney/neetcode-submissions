class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsChecked = {}
        remainder = 0

        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in numsChecked:
                return [numsChecked[remainder], i]
            
            numsChecked[nums[i]] = i
        