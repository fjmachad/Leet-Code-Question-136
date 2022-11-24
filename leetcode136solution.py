class Solution(object):
    # This method takes in a list of numbers and returns the unique number in that list
    def singleNumber(self, nums):
        my_dict = {}
        least = 1
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 0
        for j in nums:
            if j in my_dict:
                my_dict[j] += 1
        for key, value in my_dict.items():
            if value == least:
                return key
        