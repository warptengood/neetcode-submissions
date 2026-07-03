class Solution:
    def bin_less(self, target: int, arr: List[int]) -> int:
        ans = 0
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                ans = max(ans, m + 1)
                r = m - 1
            elif arr[m] < target:
                ans = max(ans, m + 1)
                l = m + 1
            else:
                r = m - 1
        return ans

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n = len(nums1) + len(nums2)
        half = n // 2 + (n % 2 != 0)
        l, r = 0, half
            
        while l <= r:
            first_half = (l + r) // 2
            second_half = half - first_half
            print(f"l={l}, r={r}, f_half: {first_half}, s_half: {second_half}")
            if len(nums1) < first_half:
                r = first_half - 1
            elif len(nums2) < second_half:
                l = first_half + 1
            else:
                first_max_element = nums1[first_half - 1] if first_half > 0 else int(-2e9)
                second_max_element = nums2[second_half - 1] if second_half > 0 else int(-2e9)
                bonus = min(
                    nums1[first_half] if first_half < len(nums1) else int(2e9), 
                    nums2[second_half] if second_half < len(nums2) else int(2e9)
                ) if n % 2 == 0 else max(first_max_element, second_max_element)

                if first_max_element == second_max_element:
                    return (first_max_element + bonus) / 2
                elif first_max_element > second_max_element:
                    n_less_elements = self.bin_less(first_max_element, nums2)
                    print(first_max_element, second_max_element, n_less_elements)
                    if n_less_elements > second_half:
                        r = first_half - 1
                    else:
                        return (first_max_element + bonus) / 2
                elif second_max_element > first_max_element:
                    n_less_elements = self.bin_less(second_max_element, nums1)
                    if n_less_elements > first_half:
                        l = first_half + 1
                    else:
                        return (second_max_element + bonus) / 2
