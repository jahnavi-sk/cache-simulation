import math


class Cache:
    def calculate_cache_bits(cache_size, main_memory_size, block_size):
        num_blocks = cache_size // block_size
        index_bits = int(math.log2(num_blocks))
        instruction_length = int(math.log2(main_memory_size))
        offset_bits = math.log2(block_size)
        tag_bits = instruction_length - offset_bits - index_bits
        return index_bits, tag_bits, offset_bits, num_blocks

    def cache_access(address, cache_size, main_memory_size, block_size, my_dictionary):
        integer = int(address, 16)
        index_bits, tag_bits, offset_bits, num_blocks = Cache.calculate_cache_bits(cache_size, main_memory_size, block_size)
        total_bits = index_bits + tag_bits + offset_bits
        total_bits = int(total_bits)
        binary_string = format(integer, f'0{total_bits}b')

        tag_bits = int(tag_bits)
        index_bits = int(index_bits)
        tag = binary_string[:tag_bits]
        index = binary_string[tag_bits:tag_bits + index_bits]
        offset = binary_string[tag_bits + index_bits:]

        index = int(index, 2)

        
        if my_dictionary[index] == -1:
            result="Miss"
            # print("Miss")
        else:
            if my_dictionary[index] == tag:
                result="Hit"

                # print("Hit")
            else:
                result="Miss"
                # print("Miss")
        my_dictionary[index] = tag 

        print(result)

        print("Memory Table is now: \n")

        print("Index    |   Tag")
        print("-------------------")
        for index, tag in my_dictionary.items():
            print(f"{index:<8} |   {tag}")
        return my_dictionary, result



if __name__ == "__main__":
    cache_size = int(input("Enter cache size: "))
    main_memory_size = int(input("Enter main memory size: "))
    block_size = int(input("Enter block size: "))

    my_dictionary = dict.fromkeys(range(cache_size // block_size), -1)
    hits = 0
    total_accesses = 0

    while True:
        address = input("Enter memory address (press -1 to exit): ")
        if address == "-1":
            break
        # cache_access(address, cache_size, main_memory_size, block_size, my_dictionary)
        my_dictionary, result = Cache.cache_access(address, cache_size, main_memory_size, block_size, my_dictionary)
        if result == "Hit":
            hits += 1
        total_accesses += 1

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0
    print(f"Hit Ratio: {hit_ratio}")
