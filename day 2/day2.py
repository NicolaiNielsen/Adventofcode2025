#get puzzle input

def get_puzzle_input():
    input = "385350926-385403705,48047-60838,6328350434-6328506208,638913-698668,850292-870981,656-1074,742552-796850,4457-6851,138-206,4644076-4851885,3298025-3353031,8594410816-8594543341,396-498,1558-2274,888446-916096,12101205-12154422,2323146444-2323289192,37-57,101-137,46550018-46679958,79-96,317592-341913,495310-629360,33246-46690,14711-22848,1-17,2850-4167,3723700171-3723785996,190169-242137,272559-298768,275-365,7697-11193,61-78,75373-110112,425397-451337,9796507-9899607,991845-1013464,77531934-77616074"
    result = [[]]
    ranges = input.split(",")
    for range_str in ranges:
        start, end = range_str.split("-")
        print(f"Range: {start} to {end}")
        result.append([start, end])
    return result


get_puzzle_input()

def has_repeating_pattern(number):
    """Check if a number contains repeating patterns like 11, 1010, 9999, 848484"""
    str_num = str(number)
    length = len(str_num)
    
    # Check for patterns of different lengths (1 to half the number length)
    for pattern_len in range(1, length // 2 + 1):
        # Extract the pattern
        pattern = str_num[:pattern_len]
        
        # Check if the entire number can be formed by repeating this pattern
        repeated_pattern = pattern * (length // pattern_len)
        
        # If the repeated pattern matches the start of our number
        if str_num.startswith(repeated_pattern) and len(repeated_pattern) >= pattern_len * 2:
            # Check if remaining part (if any) is also part of the pattern
            remaining = str_num[len(repeated_pattern):]
            if not remaining or pattern.startswith(remaining):
                return True
    
    return False

def find_pattern_numbers_in_range(start, end):
    """Find all numbers with repeating patterns in a range"""
    pattern_numbers = []
    for num in range(int(start), int(end) + 1):
        if has_repeating_pattern(num):
            pattern_numbers.append(num)
    return pattern_numbers

def get_invalid(input):
    result = 0
    all_pattern_numbers = []
    
    for i, (start, end) in enumerate(input):
        if i == 0:  # Skip the first empty list
            continue
            
        print(f"Checking range {start} to {end}...")
        pattern_numbers = find_pattern_numbers_in_range(start, end)
        print(f"Found {len(pattern_numbers)} numbers with repeating patterns")
        
        if pattern_numbers:
            print(f"First few pattern numbers: {pattern_numbers[:10]}")  # Show first 10
        
        all_pattern_numbers.extend(pattern_numbers)
        result += len(pattern_numbers)
    
    return result, all_pattern_numbers

# Test the pattern finder
ranges = get_puzzle_input()
total_patterns, all_pattern_numbers = get_invalid(ranges)
print(f"\nTotal numbers with repeating patterns: {total_patterns}")
print(f"Total pattern numbers found: {len(all_pattern_numbers)}")

# Example of some pattern numbers
if all_pattern_numbers:
    print(f"Some examples: {all_pattern_numbers[:20]}")

# Test the function with your examples
test_numbers = [11, 1010, 9999, 848484, 123, 1234]
print(f"\nTesting specific numbers:")
for num in test_numbers:
    print(f"{num}: {has_repeating_pattern(num)}")



    return result