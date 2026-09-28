class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valuesChecked = {}
        remainder = 0

        for i in range (len(nums)):
            remainder = target - nums[i]
            
            if remainder in valuesChecked:
                return [valuesChecked[remainder], i]
            valuesChecked[nums[i]] = i
                        