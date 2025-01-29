#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system
    implementing the LIFO (Last-In, First-Out) algorithm.
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key already exists, just update it
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, remove the last added item
                discarded_key = next(reversed(self.cache_data))  # Get last key added
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

            # Add the new item
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
