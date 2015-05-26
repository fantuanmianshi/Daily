"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.
"""

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.expire_queue = []

    # Move the recent visited key to the tail of queue
    def move(self, key):
        self.expire_queue.remove(key)
        self.expire_queue.append(key)

    # @return an integer
    def get(self, key):
        if key in self.data:
            self.move(key)
            return self.data[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.data:
            self.data[key] = value
            self.move(key)
            return

        if len(self.expire_queue) >= self.capacity:
            delete_key = self.expire_queue[0]
            del self.data[delete_key]
            self.expire_queue = self.expire_queue[1:]
        self.expire_queue.append(key)
        self.data[key] = value
