import math


class Cache:
    def calculate_cache_bits(cache_size, main_memory_size, block_size):
        num_blocks = cache_size // block_size
        index_bits = int(math.log2(num_blocks))
        instruction_length = int(math.log2(main_memory_size))
        offset_bits = int(math.log2(block_size))
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
        print("Tag has ",tag_bits,"bits and is: ",tag)
        index = binary_string[tag_bits:tag_bits + index_bits]
        print("Index has ",index_bits,"bits and is: ",index)
        offset = binary_string[tag_bits + index_bits:]
        print("Offset has ",offset_bits,"bits and is: ",offset)
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
        # print(index)
        return my_dictionary, result

3,6,23,42,3,4,23,57

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
        my_dictionary, result = Cache.cache_access(address, cache_size, main_memory_size, block_size, my_dictionary)
        if result == "Hit":
            hits += 1
        total_accesses += 1

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0
    print(f"Hit Ratio: {hit_ratio}")
