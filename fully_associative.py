import math

class Cache:
    def calculate_cache_bits_fully_associative(cache_size, main_memory_size, block_size):
        num_blocks = cache_size // block_size
        instruction_length = int(math.log2(main_memory_size))
        offset_bits = int(math.log2(block_size))
        block_bits = instruction_length - offset_bits 
        return block_bits, offset_bits, num_blocks

    def cache_access_fully_associative(address, cache_size, main_memory_size, block_size, my_dictionary_fully_associative,index):
        integer = int(address, 16)
        block_bits, offset_bits, num_blocks = Cache.calculate_cache_bits_fully_associative(cache_size, main_memory_size, block_size)
        total_bits = block_bits + offset_bits
        total_bits = int(total_bits)
        binary_string = format(integer, f'0{total_bits}b')

        block_bits = int(block_bits)
        offset_bits = int(offset_bits)
        block = binary_string[:block_bits]
        print("Block has ",block_bits,"bits and is: ",block)
        offset = binary_string[block_bits:]
        print("Offset has ",offset_bits,"bits and is: ",offset)

        ans =0
        for i in range(index):
            if my_dictionary_fully_associative[i] == block:
                ans=1
                result="Hit"
                break
        
        if (my_dictionary_fully_associative[index] == -1) and (ans==0):
            result="Miss"
            my_dictionary_fully_associative[index] = block
            index = (index + 1)% num_blocks
            
            # print("Miss")
        elif (my_dictionary_fully_associative[index]!= block) and (ans==0):
            result="Miss"
            my_dictionary_fully_associative[index] = block
            index = (index + 1)% num_blocks
        else:
            for i in range(0,index+1):
                if my_dictionary_fully_associative[i] == block:
                    result= "Hit"
                
        
        # elif for my_dictionary_fully_associative[index] == block:
        #         result="Hit"
        # my_dictionary_fully_associative[index] = tag 


        print(result)
        print("Memory Table is now: \n")
        # for index, (valid_bit, tag, dirty_bit) in my_dictionary_fully_associative.items():
        #     print(f"{index:<8} |   {valid_bit:<6} |   {dirty_bit:<5} |   {tag}")
        for i, tag in my_dictionary_fully_associative.items():
            print(f"{i:<8} |   {tag}")
        # print(my_dictionary_fully_associative)
        # print("Index    |   Tag")
        # print("-------------------")
        # for index, tag in my_dictionary_fully_associative.items():
        #     print(f"{index:<8} |   {block}")
        return my_dictionary_fully_associative, index, result


if __name__ == "__main__":
    cache_size = int(input("Enter cache size: "))
    main_memory_size = int(input("Enter main memory size: "))
    block_size = int(input("Enter block size: "))

    my_dictionary_fully_associative = dict.fromkeys(range(cache_size // block_size), -1)
    hits = 0
    total_accesses = 0
    index =0
    while True:
        address = input("Enter memory address (press -1 to exit): ")
        if address == "-1":
            break
        my_dictionary_fully_associative, index, result = Cache.cache_access_fully_associative(address, cache_size, main_memory_size, block_size, my_dictionary_fully_associative,index)
        if result == "Hit":
            hits += 1
        total_accesses += 1 

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0
    print(f"Hit Ratio: {hit_ratio}")
