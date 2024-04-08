class Cache:
    def __init__(self, cache_size, block_size, main_memory_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.num_blocks = cache_size // block_size
        self.cache = [None] * self.num_blocks
        self.tag = [None] * self.num_blocks
        self.dirty = [False] * self.num_blocks
        self.main_memory_size = main_memory_size

    def get_index(self, address):
        return (address // self.block_size) % self.num_blocks

    def is_hit(self, address):
        index = self.get_index(address)
        return self.cache[index] is not None and self.tag[index] == address // self.block_size

    def access(self, address):
        if self.is_hit(address):
            print("Hit")
        else:
            print("Miss")
            index = self.get_index(address)
            self.cache[index] = address
            self.tag[index] = address // self.block_size
            self.dirty[index] = False

if __name__ == "__main__":
    cache = Cache(cache_size=32, block_size=16, main_memory_size=65536) # Hardcoded values
    print("Enter memory address(press q to exit)")
    while True:
        address = int(input(""))
        if address == -1:
            break
        cache.access(address)
