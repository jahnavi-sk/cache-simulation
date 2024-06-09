# Cache Simulation

This is a code to simulate the behavior of a cache using Python scripting language. It exhibits behavior of a cache memory, considering one level of cache,

### Input

- Capacity of main memory, cache memory, and block size (in bytes)
- Memory References

### Working

- For each of the references, the binary address, the tag, and the index is identified given the mapping technique
- The Cache Hit or Cache Miss is given as output
- At the end, the hit ratio and miss ratio is displayed


### Files

`direct_mapped_cache.py` follows Direct Mapped policy

`fully_associativecache.py` follows Fully Associative policy

`cache_direct_fully_associative.py` asks the user which policy among Direct Mapped or Fully Associative they prefer
