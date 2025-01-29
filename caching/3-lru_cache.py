#!/usr/bin/env python3

"""
LRUCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that implements LRU caching.
    """

    def __init__(self):
        """
        Initializes the LRUCache instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.

        If the cache exceeds the limit, removes the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the item associated with the key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
