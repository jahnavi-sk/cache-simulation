import math


class Cache:
    def calculate_cache_bits_direct(cache_size, main_memory_size, block_size):
        num_blocks = cache_size // block_size
        index_bits = int(math.log2(num_blocks))
        instruction_length = int(math.log2(main_memory_size))
        offset_bits = int(math.log2(block_size))
        tag_bits = instruction_length - offset_bits - index_bits
        return index_bits, tag_bits, offset_bits, num_blocks

    def calculate_cache_bits_fully_associative(cache_size, main_memory_size, block_size):
        num_blocks = cache_size // block_size
        instruction_length = int(math.log2(main_memory_size))
        offset_bits = int(math.log2(block_size))
        block_bits = instruction_length - offset_bits 
        return block_bits, offset_bits, num_blocks

    def cache_access_direct(address, cache_size, main_memory_size, block_size, my_dictionary):
        integer = int(address, 16)
        index_bits, tag_bits, offset_bits, num_blocks = Cache.calculate_cache_bits_direct(cache_size, main_memory_size, block_size)
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

    def cache_access_fully_associative(address, cache_size, main_memory_size, block_size, my_dictionary,index):
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
            if my_dictionary[i] == block:
                ans=1
                result="Hit"
                break
        
        if (my_dictionary[index] == -1) and (ans==0):
            result="Miss"
            my_dictionary[index] = block
            index = (index + 1)% num_blocks
            
            # print("Miss")
        elif (my_dictionary[index]!= block) and (ans==0):
            result="Miss"
            my_dictionary[index] = block
            index = (index + 1)% num_blocks
        else:
            for i in range(0,index+1):
                if my_dictionary[i] == block:
                    result= "Hit"
                
        
        # elif for my_dictionary[index] == block:
        #         result="Hit"
        # my_dictionary[index] = tag 


        print(result)
        print("Memory Table is now: \n")
        # for index, (valid_bit, tag, dirty_bit) in my_dictionary.items():
        #     print(f"{index:<8} |   {valid_bit:<6} |   {dirty_bit:<5} |   {tag}")
        for i, tag in my_dictionary.items():
            print(f"{i:<8} |   {tag}")
        # print(my_dictionary)
        # print("Index    |   Tag")
        # print("-------------------")
        # for index, tag in my_dictionary.items():
        #     print(f"{index:<8} |   {block}")
        return my_dictionary, index, result

if __name__ == "__main__":

    choice = int(input("Would you like to proceed with direct mapping[1] or fully associative mapping with FIFO policy[2] : "))

    cache_size = int(input("Enter cache size: "))
    main_memory_size = int(input("Enter main memory size: "))
    block_size = int(input("Enter block size: "))


    my_dictionary = dict.fromkeys(range(cache_size // block_size), '-')
    hits = 0
    total_accesses = 0
    index =0

    while True:
        address = input("Enter memory address (press -1 to exit): ")
        if address == "-1":
            break
        if choice==1:
            my_dictionary, result = Cache.cache_access_direct(address, cache_size, main_memory_size, block_size, my_dictionary)
        elif choice==2:
            my_dictionary, index, result = Cache.cache_access_fully_associative(address, cache_size, main_memory_size, block_size, my_dictionary,index)

        if result == "Hit":
            hits += 1
        total_accesses += 1

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0
    print(f"Hit Ratio: {hit_ratio}")
    print("Miss Ratio:", 1-hit_ratio)
