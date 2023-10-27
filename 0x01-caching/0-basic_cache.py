#!/usr/bin/python3
"""Basic Cache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a class BasicCache that inherits from BaseCaching
        Defines Caching system
    """

    def put(self, key, item):
        """Add item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item"""
        if key is not None:
            return self.cache_data.get(key)
