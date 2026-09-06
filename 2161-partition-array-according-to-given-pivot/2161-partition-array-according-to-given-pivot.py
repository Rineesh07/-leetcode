class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        n = len(nums)
        for i in range(n):
            if nums[i] < pivot :
                list1.append(nums[i])
            elif nums[i] > pivot:
                list2.append(nums[i])
            else:
                list3.append(nums[i])
        partition = list1+list3+list2
        return partition
        