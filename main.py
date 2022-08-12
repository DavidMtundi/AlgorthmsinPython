#this is to find the possible set of numbers that add up to get the given sum provided
#i.e in this set {1,2,3,3,4,4} and the required sum is 7, the answer is 3 and 4
class Solution():
    def findMedianSortedArrays( nums1, nums2):
        num3 = []
        for num in nums1:
            num3.append(num)
        for num in nums2:
            num3.append(num)
        num3.sort()
        print(num3)
        value = len(num3)/2
        print(num3[value])


Solution.findMedianSortedArrays([1,2,3],[2])