import random

class RandomizedSet(object):

    def __init__(self):
        # Stores the actual values for O(1) random access
        self.data_list = []
        # Maps value -> its index in data_list for O(1) lookup/removal
        self.data_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_map:
            return False
        
        # Add to the map and append to the list
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data_map:
            return False
        
        # 1. Get index of the element to remove and the last element
        idx_to_remove = self.data_map[val]
        last_element = self.data_list[-1]
        
        # 2. Move the last element to the spot of the element we're removing
        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove
        
        # 3. Remove the last element from both structures
        self.data_list.pop()
        del self.data_map[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        # random.choice works in O(1) on a list
        return random.choice(self.data_list)