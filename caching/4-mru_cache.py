#!/usr/bin/env python3
"""
This module contains the implementation of the MRUCache class.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements MRU caching.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        and discards the most recently used item
        If the cache exceeds the limit, removes the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                self.cache_data.pop(mru_key)
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the item associated with the key.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
