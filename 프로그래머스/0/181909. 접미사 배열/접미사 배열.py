def solution(my_string):
    # Step 1: Generate all suffixes
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # Step 2: Sort the suffixes in lexicographical order
    suffixes.sort()
    
    # Step 3: Return the sorted suffixes
    return suffixes