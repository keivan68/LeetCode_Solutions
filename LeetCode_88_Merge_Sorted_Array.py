class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_m = nums1[0:m]
        pointer1 = 0
        pointer2 = 0
        i = 0
        while pointer1 < m and pointer2 < n:
            if nums1_m[pointer1] < nums2[pointer2]:
                nums1[i] = nums1_m[pointer1]
                pointer1 += 1
            elif nums1_m[pointer1] > nums2[pointer2]:
                nums1[i] = nums2[pointer2]
                pointer2 += 1
            elif nums1_m[pointer1] == nums2[pointer2]:
                nums1[i] = nums1_m[pointer1]
                i += 1
                nums1[i] = nums2[pointer2]
                pointer1 += 1
                pointer2 += 1
            i += 1
        if pointer1 < m:
            nums1[(n+pointer1):] = nums1_m[pointer1:m]
        if pointer2 < n:
            nums1[(m+pointer2):] = nums2[pointer2:n]
        
