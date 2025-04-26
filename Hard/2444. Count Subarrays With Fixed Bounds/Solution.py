class Solution(object):
  def countSubarrays(self, nums, minK, maxK):
      """
      :type nums: List[int]
      :type minK: int
      :type maxK: int
      :rtype: int
      """
      min_pos = -1
      max_pos = -1
      bad_pos = -1
      count = 0

      for i, num in enumerate(nums):
          if num < minK or num > maxK:
              bad_pos = i
          if num == minK:
              min_pos = i
          if num == maxK:
              max_pos = i

          valid_start = min(min_pos, max_pos)
          if valid_start > bad_pos:
              count += valid_start - bad_pos

      return count
