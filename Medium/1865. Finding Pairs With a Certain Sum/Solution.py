from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)  # frequency map of nums2

    def add(self, index, val):
        old_val = self.nums2[index]
        new_val = old_val + val
        
        # Update the frequency map
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.counter2[new_val] += 1

        # Update nums2
        self.nums2[index] = new_val

    def coaunt(self, tot):
        r = 0
        for a in self.nums1:
            complement = tot - a
            r += self.counter2.get(complement, 0)
        return r
