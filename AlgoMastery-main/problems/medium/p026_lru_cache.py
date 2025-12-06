"""
Task 26: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the LRUCache class with the following methods:
- get(key): Return the value of the key if it exists, otherwise return -1.
- put(key, value): Update the value of the key if it exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity, evict the least recently used key.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1) -> 1
    cache.put(3, 3) # evicts key 2
    cache.get(2) -> -1
    cache.put(4, 4) # evicts key 1
    cache.get(1) -> -1
    cache.get(3) -> 3
    cache.get(4) -> 4

Args:
    capacity (int): Maximum number of keys in the cache (0-indexed)

Returns:
    class: LRUCache class with get and put methods
"""

class LRUCache:
    """
    LRU Cache.

    Args:
        capacity (int): Maximum number of keys in the cache (0-indexed)

    Methods:
        get(key: int) -> int
        put(key: int, value: int) -> None
    """
    def __init__(self, capacity: int):
            self.d={}
            self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.d:
            vall=self.d[key]
            self.d.pop(key)
            self.d[key]=vall
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
          self.d.pop(key)  
          self.d[key]=value
        
        elif len(self.d) >= self.capacity:
            first_key=next(iter(self.d))
            self.d.pop(first_key)
            self.d[key]=value
        else:
            self.d[key]=value
